import { Tabs, Box } from "@bigcommerce/big-design";
import { useState } from "react";
import OrderList from "./orderList";
import Summary from "./summary";

function Layout() {
  const [activeTab, setActiveTab] = useState("tab1");

  const items = [
    { id: "tab1", title: "Summary" },
    { id: "tab2", title: "Order List" },
  ];

  return (
    <div style={{ backgroundColor: "#F6F7F9", height: "100vh" }}>
      <div style={{ marginLeft: "50px" }}>
        <h1
          style={{
            color: "#313440",
            fontSize: "1.5rem",
            fontWeight: 400,
            lineHeight: "2rem",
            marginTop: "0",
            paddingTop: "16px",
          }}
        >
          Sample App
        </h1>
      </div>
      <div style={{ marginLeft: "50px" }}>
        <Tabs activeTab={activeTab} items={items} onTabClick={setActiveTab} />
      </div>
      <div style={{ marginLeft: "50px" }}>
        <Box marginTop="large">
          {activeTab === "tab1" && <Summary />}
          {activeTab === "tab2" && <OrderList />}
        </Box>
      </div>
    </div>
  );
}

export default Layout;
