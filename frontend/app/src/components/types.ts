export interface Customer {
    id: number;
    first_name: string;
    last_name: string;
    patronymic: string;
    nickname: string;
    sex: boolean;
    deleted: boolean;
}

export interface Order {
    id: number;
    customer_id: number;
    total: number;
    code: string;
    deleted: boolean;
}