import { Tabs, Box, H0 } from "@bigcommerce/big-design";
import { useState } from "react";
import OrderList from "./orderList";
import Summary from "./summary";




function  Layout() {
  const [activeTab, setActiveTab] = useState('tab1');

  const items = [
    { id: 'tab1', title: 'Summary' },
    { id: 'tab2', title: 'Order List' },      
  ];

  return (
    <div style={{'margin': '2% 25%'}}>
      <H0>Inventory Management App</H0>
      <Tabs activeTab={activeTab} items={items} onTabClick={setActiveTab} />
      <Box marginTop="large">
        {activeTab === 'tab1' && <Summary />}
        {activeTab === 'tab2' && <OrderList />}
      </Box>
    </div>
  );
}

export default Layout