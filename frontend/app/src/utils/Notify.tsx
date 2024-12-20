import React from "react";
import {Message, toaster} from "rsuite";
import {ToastContainerProps} from "rsuite/cjs/toaster/ToastContainer";

const messageProps: ToastContainerProps = {
    placement: "bottomEnd",
    duration: 10_000,
}

export class Notify {
    public static Info(message: string) {
        const messageTemplate = (
            <Message
                type={"info"}
                closable={true}
            >
                {message}
            </Message>
        );
        toaster.push(messageTemplate, messageProps);
    }

    public static Success(message: string) {
        const messageTemplate = (
            <Message
                type={"success"}
                closable={true}
            >
                {message}
            </Message>
        );
        toaster.push(messageTemplate, messageProps);
    }

    public static Error(message: string) {
        const messageTemplate = (
            <Message
                type={"error"}
                closable={true}
            >
                {message}
            </Message>
        );
        toaster.push(messageTemplate, messageProps);
    }

    public static Warning(message: string) {
        const messageTemplate = (
            <Message
                type={"warning"}
                closable={true}
            >
                {message}
            </Message>
        );
        toaster.push(messageTemplate, messageProps);
    }
}