import { Button, Table } from "@bigcommerce/big-design";
import { useState, useEffect } from "react";
import Loader from "./loader";


function getList() {
    return fetch('/bc-api/v2/orders')
      .then(data => data.json())
} 



function orderUpdate(orderId){
  return fetch(`/bc-api/v2/orders/${orderId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ status_id: 5 }),
  })
}




function OrderList() {


    const [currentPage, setCurrentPage] = useState(1);
    const [itemsPerPageOptions] = useState([5, 10, 20, 30]);
    const [itemsPerPage, setItemsPerPage] = useState(5);
    const [currentItems, setCurrentItems] = useState([]);
    const [loading, setLoading] = useState(true)
    const [data, setList] = useState([]);

    const columns=[
        { header: 'Order Id', hash: 'id', render: ({ id }) => id },
        { header: 'Billing Name', hash: 'billing_address', render: ({ billing_address }) =>`${ billing_address.first_name} ${billing_address.last_name}` },
        { header: 'Order Total', hash: 'total_tax', render: ({ total_tax }) => total_tax },
        { header: 'Order Status', hash: 'custom_status', render: ({ custom_status }) => custom_status },
        { header: 'Action', hash: 'stock', render: ({ id }) => <Button actionType="destructive" onClick={() => orderUpdate(id).then(setLoading(true))} >Cancel</Button> },
    ]

        

    const onItemsPerPageChange = (newRange) => {
      setCurrentPage(1);
      setItemsPerPage(newRange);
    };

  
    useEffect(() => {
    getList().then(items => {
        setList(items);
        const maxItems = currentPage * itemsPerPage;
        const lastItem = Math.min(maxItems, items.length);
        const firstItem = Math.max(0, maxItems - itemsPerPage);
        setCurrentItems(items.slice(firstItem, lastItem));
    }).then(() => setLoading(false))
    }, [currentPage, itemsPerPage, loading]);
  
    return (
      <>
      { loading ? <Loader /> 
      :
      <Table
        keyField="sku"
        columns={columns}
        items={currentItems}
        itemName="Orders"
        pagination={{
          currentPage,
          totalItems: data.length,
          onPageChange: setCurrentPage,
          itemsPerPageOptions,
          onItemsPerPageChange,
          itemsPerPage,
        }}
        stickyHeader
      />
    }
    </>
    );
  }
  

  export default OrderList;