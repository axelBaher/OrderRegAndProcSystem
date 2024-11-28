import React from "react";
import {useNavigate} from 'react-router-dom';
import {QueryClient, QueryClientProvider} from "@tanstack/react-query";
import {ReactQueryDevtools} from "@tanstack/react-query-devtools"
import "rsuite/dist/rsuite.min.css"
import Main from "./Main"
import {Navbar, Nav} from "rsuite";

const App: React.FC = () => {
    const queryClient = new QueryClient();
    const navigate = useNavigate();
    return (
        <QueryClientProvider client={queryClient}>
            <>
                <div>
                    <Navbar>
                        <Nav>
                            <Nav.Item onClick={() => {
                                navigate("/customers")
                            }}>Customers</Nav.Item>
                            <Nav.Item onClick={() => {
                                navigate("/orders")
                            }}>Orders</Nav.Item>
                            <Nav.Item onClick={() => {
                                navigate("/customer")
                            }}>Customer Info</Nav.Item>
                        </Nav>
                    </Navbar>
                    <hr/>
                    <Main/>
                </div>
            </>
            <ReactQueryDevtools initialIsOpen={false}/>
        </QueryClientProvider>
    );
};

export default App;