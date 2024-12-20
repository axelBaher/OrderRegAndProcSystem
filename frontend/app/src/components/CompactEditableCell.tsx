import React, {useEffect, useState} from "react";
import {Table} from "rsuite";

interface CompactCellProps extends React.ComponentProps<typeof Table.Cell> {
    editable?: boolean,
    rowData: any,
    dataKey: string,
    onEdit?: (id: number, key: string, value: any) => void,
    render?: (rowData: any, refetch?: (props:any) => any) => React.ReactNode;
}

const CompactCell: React.FC<CompactCellProps> = ({
                                                     editable = false,
                                                     rowData,
                                                     dataKey,
                                                     onEdit,
                                                     render,
                                                     ...props
                                                 }) => {
    const [isEditing, setIsEditing] = useState(false);
    const [value, setValue] = useState(rowData[dataKey]);

    useEffect(() => {
        setValue(rowData[dataKey] ?? "");
    }, [rowData, dataKey]);


    const handleBlur = () => {
        setIsEditing(false);
        if (onEdit) {
            onEdit(rowData.id, dataKey, value);
        }
    };

    return (
        <Table.Cell {...props} style={{
            padding: 6,
            cursor: editable ? "pointer" : "default",
            backgroundColor: editable ? "inherit" : "#f9f9f9",
            color: editable ? "#636363" : "inherit",
            border: "10px",
        }}>
            {editable && isEditing ? (
                <input
                    type="text"
                    value={value}
                    onChange={(e) => setValue(e.target.value)}
                    onBlur={handleBlur}
                    onKeyDown={(e) => e.key === "Enter" && handleBlur()}
                    autoFocus
                    style={{
                        width: "100%",
                        padding: "4px",
                        // boxSizing: "border-box",
                        // border: "none",
                        // outline: "none",
                    }}
                />
            ) : (
                <span onDoubleClick={() => editable && setIsEditing(true)}
                      style={{
                          display: rowData[dataKey] ? "inline" : "inline-block",
                          minHeight: "20px",
                          width: "100%"
                      }}>
                {render
                    ? render(rowData)
                    : rowData[dataKey]}
                </span>
            )}
        </Table.Cell>
    );
};

export default CompactCell;