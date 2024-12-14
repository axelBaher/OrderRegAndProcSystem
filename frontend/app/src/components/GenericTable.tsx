// GenericTable.tsx
import React from "react";
import {useQuery} from "@tanstack/react-query";
import {
    Table,
    Loader,
} from "rsuite";

interface GenericTableProps<T> {
    fetchData: () => Promise<T[]>;
    columns: TableColumn<T>[];
    queryKey: string[];
    tableTitle: string;
    onAdd?: (newItem: Partial<T>) => Promise<void>;
    enableAdd?: boolean;
}


export interface TableColumn<T> {
    title: string;
    dataKey: Extract<keyof T, string>;
    width?: number;
    fixed?: boolean;
    align?: "left" | "center" | "right";
    render?: (rowData: T) => React.ReactNode;
}

const GenericTable = <T extends object>({
                                            fetchData,
                                            columns,
                                            queryKey,
                                            tableTitle,
                                        }: GenericTableProps<T>) => {
    const [sortColumn, setSortColumn] = React.useState();
    const [sortType, setSortType] = React.useState();
    const [loading, setLoading] = React.useState(false);
    const {data, isLoading, error} = useQuery<T[], Error>({
        queryKey,
        queryFn: fetchData,
        refetchOnWindowFocus: false
    });
    const handleSortColumn = (sortColumn: any, sortType: any) => {
        setLoading(true);
        setTimeout(() => {
            setLoading(false);
            setSortColumn(sortColumn);
            setSortType(sortType);
        }, 500);
    };
    const getData = <T extends Record<string, any>>(data: T[], sortColumn?: keyof T, sortType?: "asc" | "desc"): T[] => {
        if (sortColumn && sortType) {
            return data.sort((a, b) => {
                let x = a[sortColumn];
                let y = b[sortColumn];
                if (sortType === 'asc') {
                    return x - y;
                } else {
                    return y - x;
                }
            });
        }
        return data;
    };
    if (isLoading) {
        return <Loader center content="Loading..."/>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    if (!data) {
        return <div>No data to display</div>;
    }

    return (
        <div>
            <h1>{tableTitle}</h1>
            <Table
                data={getData(data, sortColumn, sortType)}
                autoHeight={true}
                sortColumn={sortColumn}
                sortType={sortType}
                onSortColumn={handleSortColumn}
                loading={loading}>
                {columns.map((column, index) => (
                    <Table.Column
                        key={index}
                        width={column.width}
                        fixed={column.fixed}
                        align={column.align}
                        resizable
                        sortable
                    >
                        <Table.HeaderCell>{column.title}</Table.HeaderCell>
                        <Table.Cell dataKey={column.dataKey}>
                            {(rowData: T) =>
                                column.render
                                    ? column.render(rowData)
                                    : rowData[column.dataKey] as React.ReactNode
                            }
                        </Table.Cell>
                    </Table.Column>
                ))}
            </Table>
        </div>
    );
};

export default GenericTable;