import React from "react";
import {useQuery} from "@tanstack/react-query";
import {Table, Loader} from "rsuite";

interface GenericTableProps<T> {
    fetchData: () => Promise<T[]>;
    columns: TableColumn<T>[];
    queryKey: string[];
    tableTitle: string;
}


export interface TableColumn<T> {
    title: string;
    dataKey: keyof T;
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
    const {data, isLoading, error} = useQuery<T[], Error>({
        queryKey,
        queryFn: fetchData,
    });

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
            <Table data={data} autoHeight={true}>
                {columns.map((column, index) => (
                    <Table.Column
                        key={index}
                        width={column.width}
                        fixed={column.fixed}
                        align={column.align}
                    >
                        <Table.HeaderCell>{column.title}</Table.HeaderCell>
                        <Table.Cell>
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