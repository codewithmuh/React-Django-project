import { Tabs, Box, Text } from "@bigcommerce/big-design";
import { useState } from "react";
import TestComp from "./components/testcomp";
import  Home  from "./screens/home";

function  Layout() {
  const [activeTab, setActiveTab] = useState('tab1');

  const items = [
    { id: 'tab1', title: 'Summary' },
    { id: 'tab2', title: 'Order List' },      
  ];

  return (
    <div style={{'margin': '2% 25%'}}>
      <Tabs activeTab={activeTab} items={items} onTabClick={setActiveTab} />
      <Box marginTop="large">
        {activeTab === 'tab1' && <Home />}
        {activeTab === 'tab2' && <TestComp />}
      </Box>
    </div>
  );
}

export default Layout