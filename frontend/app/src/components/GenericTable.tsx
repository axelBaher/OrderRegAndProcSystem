// GenericTable.tsx
import React, {useEffect, useMemo, useState} from "react";
import {QueryObserverResult, RefetchOptions, useQuery} from "@tanstack/react-query";
import {
    Table,
    Loader, Button, IconButton, Stack,
} from "rsuite";
import axiosInstance from "../api/axiosInstance";
import {EntityType} from "./types";
import PlusIcon from '@rsuite/icons/Trash';
import CompactCell from "./CompactEditableCell";
import {AddressAddModal} from "../pages/modal/AddressAddModal";
import {getCustomerID} from "../pages/CustomerDetails";
import {ContactAddModal} from "../pages/modal/ContactAddModal";

export interface TableColumn<T> {
    title: string,
    dataKey: Extract<keyof T, string>,
    width?: number,
    fixed?: boolean,
    align?: "left" | "center" | "right",
    render?: (rowData: any, refetch?: (props: any) => any) => React.ReactNode,
    editable?: boolean,
    visible?: boolean;
}

interface GenericTableProps<T> {
    fetchData: () => Promise<T[]>,
    saveData?: (data: T[]) => Promise<void>,
    columns: TableColumn<T>[],
    queryKey: string[],
    tableTitle: string,
    onAdd?: (newItem: Partial<T>) => Promise<void>,
    enableAdd?: boolean;
}

function getEndpoint(item: any) {
    let endpoint = null;
    switch (item.eType) {
        case "Customers":
            endpoint = `/customers/${item.id ?? ""}`;
            break;
        case "Addresses":
            endpoint = `/customers/${item.customer_id}/addresses/${item.id ?? ""}`;
            break;
        case "Contacts":
            endpoint = `/customers/${item.customer_id}/contacts/${item.id ?? ""}`;
            break;
        case "Orders":
            endpoint = `/customers/${item.customer_id}/orders/${item.id ?? ""}`;
            break;
        default:
            console.log("getEndpoint")
            console.log(item.eType)
            return ""
    }
    return endpoint;
}

export const saveData = async <T extends { id: number | undefined | null, eType: EntityType | undefined | null }>(
    // endpoint: string,
    data: T[]
): Promise<void> => {
    // try {
    //     const updatePromise = data.map((item) =>
    //         axiosInstance.put(`https://127.0.0.1:8000${endpoint}`, item)
    //     );
    //     const promise = await Promise.all(updatePromise);
    //     const status = promise.map((result) => result.status)[0];
    //     if (status === 204) { // noinspection ExceptionCaughtLocallyJS
    //         return Promise.reject("Data not found");
    //     }
    //     console.log("All changes saved successfully.");
    // } catch (error) {
    //     console.error("Failed to save changes:", error);
    //     throw new Error("Failed to save changes. Please try again.");
    // }
    try {
        data.map(async (item: any) => {
            const endpoint = getEndpoint(item);
            console.log("saveData");
            console.log(item);
            if (item.id) {
                const updateResult = await axiosInstance.put(`https://127.0.0.1:8000${endpoint}`, item);
                if (updateResult.status === 204) {
                    return Promise.reject("Data not found");
                }
            } else {
                const createResult = await axiosInstance.post(`https://127.0.0.1:8000${endpoint}`, item);
                if (createResult.status === 204) {
                    return Promise.reject("Data not found");
                }
            }
        });
    } catch (error) {
        throw new Error("Error");
    }
};

export const deleteData = async (
    item: any,
    refetch?: (options?: any) => any,
): Promise<void> => {
    const endpoint = getEndpoint(item);
    const createResult = await axiosInstance.delete(`https://127.0.0.1:8000${endpoint}`, item);
    if (createResult.status === 204) {
        return Promise.reject("Data not found");
    }
    if (refetch) {
        await refetch();
    }
}

const GenericTable = <T extends { id: number | undefined | null, eType: EntityType | undefined | null }
>({
      fetchData,
      saveData,
      columns,
      queryKey,
      tableTitle
  }: GenericTableProps<T>) => {
    const {data, isLoading, error, refetch} = useQuery<T[], Error>({
        queryKey,
        queryFn: fetchData,
        refetchOnWindowFocus: false
    });
    const [loading] = React.useState(false);

    const [sortColumn, setSortColumn] = useState<keyof T | null>(null);
    const [sortType, setSortType] = useState<"asc" | "desc" | null>(null);

    const [originalData, setOriginalData] = useState<T[]>([]);
    const [editableData, setEditableData] = useState<T[]>([]);
    const [hasChanges, setHasChanges] = useState(false);
    const [saving, setSaving] = useState(false);

    const [AddressAddModalIsOpen, setAddressAddModalIsOpen] = useState(false);
    const [ContactAddModalIsOpen, setContactAddModalIsOpen] = useState(false);

    useEffect(() => {
        if (data) {
            setEditableData(data);
            setOriginalData(data);
        }
    }, [data]);

    const sortedData = useMemo(() => {
        if (!sortColumn || !sortType) return editableData;

        return [...editableData].sort((a, b) => {
            const x = a[sortColumn];
            const y = b[sortColumn];

            if (x == null || y == null) return 0;

            // if (typeof x === "number" && typeof y === "number") {
            //     return sortType === "asc" ? x - y : y - x;
            // }

            return sortType === "asc"
                ? String(x).localeCompare(String(y))
                : String(y).localeCompare(String(x));
        });
    }, [editableData, sortColumn, sortType]);

    const handleSortColumn = (column: keyof T, type: "asc" | "desc") => {
        setSortColumn(column);
        setSortType(type);
    };

    const handleCellChange = (id: number, key: string, value: any) => {
        const nextData = editableData.map((item) => {
                // console.log("item.id = " + JSON.stringify(item.id));
                // console.log("id = " + JSON.stringify(id));
                return item.id === id ? {...item, [key]: value} : item;
            }
        );
        setEditableData(nextData);
        setHasChanges(true);
    };

    const getChangedData = () => {
        return editableData.filter((item) => {
            const originalItem = originalData.find((orig) => orig.id === item.id);
            return (
                originalItem && JSON.stringify(item) !== JSON.stringify(originalItem)
            );
        });
    };

    const handleSave = async () => {
        if (!saveData) {
            alert("Changes saved successfully (no)!");
            setHasChanges(false);
            return;
        }
        console.log("handleSave")
        const changedData = getChangedData();

        if (changedData.length === 0) {
            alert("No changes to save.");
            setHasChanges(false);
            return;
        }

        setSaving(true);
        try {
            await saveData(changedData);
            setOriginalData(editableData);
            setHasChanges(false);
            alert("Changes saved successfully!");
        } catch (error) {
            console.error("Failed to save changes:", error);
            alert("Failed to save changes. Please try again.");
        } finally {
            setSaving(false);
        }
    };

    if (isLoading) {
        return <Loader center content="Loading..."/>;
    }
    if (error) {
        return <div>Error: {error.message}</div>;
    }
    // if (!data) {
    //     return <div>No data to display</div>;
    // }


    return (
        <div>
            <AddressAddModal
                parentID={getCustomerID()}
                refetch={refetch}
                show={AddressAddModalIsOpen}
                onCancel={() => setAddressAddModalIsOpen(false)}
                onSubmit={() => setAddressAddModalIsOpen(false)}
            />
            <ContactAddModal
                parentID={getCustomerID()}
                refetch={refetch}
                show={ContactAddModalIsOpen}
                onCancel={() => setContactAddModalIsOpen(false)}
                onSubmit={() => setContactAddModalIsOpen(false)}
            />

            <Stack
                justifyContent="flex-start"
                spacing={10}
                alignItems="center">
                <h1>{tableTitle}</h1>
                {tableTitle === "Customer" ? <></> :
                    <div>
                        <Button size={"lg"} onClick={() => {
                            switch (tableTitle) {
                                case "Addresses":
                                    setAddressAddModalIsOpen(true);
                                    break;
                                case "Contacts":
                                    setContactAddModalIsOpen(true);
                            }
                        }}>Add</Button>
                    </div>
                }
            </Stack>
            <Table
                data={sortedData}
                autoHeight={true}
                sortColumn={sortColumn as string | undefined}
                sortType={sortType as any}
                onSortColumn={handleSortColumn as any}
                loading={loading}>
                {columns.map((column, index) => (
                    column.visible === false ? (<></>) : (
                        <Table.Column
                            key={index}
                            width={column.width}
                            fixed={column.fixed}
                            align={column.align}
                            resizable
                            sortable
                            fullText
                        >
                            <Table.HeaderCell>{column.title}</Table.HeaderCell>
                            <CompactCell
                                dataKey={column.dataKey}
                                rowData={data}
                                editable={column.editable}
                                onEdit={handleCellChange}
                                render={(rowData) => column?.render?.(rowData, refetch) ?? rowData[column.dataKey]}
                            />
                        </Table.Column>
                    )
                ))
                }
            </Table>
            {hasChanges && (
                <div style={{marginTop: "10px", textAlign: "left"}}>
                    <Button
                        appearance="primary"
                        onClick={handleSave}
                        loading={saving}
                        disabled={saving}
                    >
                        Save Changes
                    </Button>
                </div>
            )}
        </div>
    );
};

export default GenericTable;