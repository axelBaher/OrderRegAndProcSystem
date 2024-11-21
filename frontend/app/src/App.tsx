import React from "react";
import {QueryClient, QueryClientProvider} from "@tanstack/react-query";
import {ReactQueryDevtools} from "@tanstack/react-query-devtools"
import CustomersPage from "./pages/Customers";
import "rsuite/dist/rsuite.min.css"


const App: React.FC = () => {
    // const queryClient = new QueryClient();
    return (<div></div>
        // <QueryClientProvider client={queryClient}>
        //     <CustomersPage/>
        //     <ReactQueryDevtools initialIsOpen={false}/>
        // </QueryClientProvider>
    );
};

export default App;