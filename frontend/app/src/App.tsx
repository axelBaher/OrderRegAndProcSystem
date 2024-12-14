// App.tsx
import React from "react";
import {QueryClient, QueryClientProvider} from "@tanstack/react-query";
import {ReactQueryDevtools} from "@tanstack/react-query-devtools"
import "rsuite/dist/rsuite.min.css"
import Main from "./Main"
import {AuthProvider} from "./components/AuthContext";
import Navigation from "./components/Navigation";


const App: React.FC = () => {
    const queryClient = new QueryClient();

    return (
        <AuthProvider>
            <QueryClientProvider client={queryClient}>
                <>
                    <div>
                        <Navigation/>
                        <hr/>
                        <Main/>
                    </div>
                </>
                <ReactQueryDevtools initialIsOpen={false}/>
            </QueryClientProvider>
        </AuthProvider>
    );
};

export default App;
