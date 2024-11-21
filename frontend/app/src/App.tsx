import React from "react";
import {Link} from 'react-router-dom';
import {QueryClient, QueryClientProvider} from "@tanstack/react-query";
import {ReactQueryDevtools} from "@tanstack/react-query-devtools"
// import "rsuite/dist/rsuite.min.css"
import Main from "./Main"


const App: React.FC = () => {
    const queryClient = new QueryClient();
    return (
        <QueryClientProvider client={queryClient}>
            <>
                <div>
                    <ul>
                        <li><Link to="/customers">Customers</Link></li>
                        <li><Link to="/orders">Orders</Link></li>
                    </ul>
                    <hr/>
                    <Main/>
                </div>
            </>
            <ReactQueryDevtools initialIsOpen={false}/>
        </QueryClientProvider>
    );
};

export default App;