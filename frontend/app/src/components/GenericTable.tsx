// GenericTable.tsx
import React, {useEffect, useMemo, useState} from "react";
import {useQuery} from "@tanstack/react-query";
import {
    Table,
    Loader, Button,
} from "rsuite";
import CompactCell from "./CompactEditableCell";
import axiosInstance from "../api/axiosInstance";

export interface TableColumn<T> {
    title: string,
    dataKey: Extract<keyof T, string>,
    width?: number,
    fixed?: boolean,
    align?: "left" | "center" | "right",
    render?: (rowData: T) => React.ReactNode,
    editable?: boolean;
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

export const saveData = async <T extends { id: number }>(
    endpoint: string,
    data: T[]
): Promise<void> => {
    try {
        const updatePromises = data.map((item) =>
            axiosInstance.put(`https://127.0.0.1:8000${endpoint}`, item)
        );

        await Promise.all(updatePromises);

        console.log("All changes saved successfully.");
    } catch (error) {
        console.error("Failed to save changes:", error);
        throw new Error("Failed to save changes. Please try again.");
    }
};

const GenericTable = <T extends { id: number }>({
                                                    fetchData,
                                                    saveData,
                                                    columns,
                                                    queryKey,
                                                    tableTitle
                                                }: GenericTableProps<T>) => {
    const {data, isLoading, error} = useQuery<T[], Error>({
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
        const nextData = editableData.map((item) =>
            item.id === id ? {...item, [key]: value} : item
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
            <h1>{tableTitle}</h1>
            <Table
                data={sortedData}
                autoHeight={true}
                sortColumn={sortColumn as string | undefined}
                sortType={sortType as any}
                onSortColumn={handleSortColumn as any}
                loading={loading}>
                {columns.map((column, index) => (
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
                            render={column.render}
                        />
                    </Table.Column>
                ))}
            </Table>
            {hasChanges && (
                <div style={{marginTop: "10px", textAlign: "right"}}>
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