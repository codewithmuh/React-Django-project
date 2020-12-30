import {
  Button,
  Table,
  Panel,
  Modal,
  Text,
  createAlertsManager,
  AlertsManager,
  Badge,
} from "@bigcommerce/big-design";
import { useState, useEffect } from "react";
import Loader from "./loader";

const alertsManager = createAlertsManager();

function getList() {
  return fetch(`/bc-api/v2/orders`).then((data) => data.json());
}

function orderUpdate(orderId) {
  return fetch(`/bc-api/v2/orders/${orderId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ status_id: 5 }),
  });
}

function orderDelete(orderId) {
  return fetch(`/bc-api/v2/orders/${orderId}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  });
}

function AddAlert(title, details, type) {
  const alert = {
    header: title,
    messages: [
      {
        text: details,
      },
    ],
    type: type,
    onClose: () => null,
    autoDismiss: true,
  };
  return alertsManager.add(alert);
}

function orderStatus(status, is_deleted) {
  if (is_deleted) {
    return <div></div>;
  } else {
    switch (status) {
      case "Completed":
        return <Badge variant="success" label={status} />;
        break;
      case "Awaiting Fulfillment":
        return <Badge variant="secondary" label={status} />;
        break;
      case "Cancelled":
        return <Badge variant="danger" label={status} />;
        break;
      default:
        return <Badge variant="secondary" label={status} />;
    }
  }
}

function OrderList() {
  const [currentPage, setCurrentPage] = useState(1);
  const [itemsPerPageOptions] = useState([5, 10, 20, 30]);
  const [itemsPerPage, setItemsPerPage] = useState(5);
  const [currentItems, setCurrentItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [data, setList] = useState([]);

  function DeleteAlert() {
    AddAlert("Order Delete", "Order Has Been Deleted Successfully!", "success");
  }
  function UpdateAlert() {
    AddAlert(
      "Order Update",
      "Order Has Been Cancelled Successfully!",
      "success"
    );
  }

  function DeleteButton(id, is_deleted) {
    const [isOpen, setIsOpen] = useState(false);

    if (!is_deleted) {
      return (
        <>
          <Button
            onClick={() => setIsOpen(true)}
            variant="subtle"
            actionType="destructive"
          >
            Delete Order
          </Button>

          <Modal
            actions={[
              {
                text: "Cancel",
                variant: "subtle",
                onClick: () => setIsOpen(false),
              },
              {
                text: "Delete",
                onClick: () =>
                  orderDelete(id)
                    .then(setIsOpen(false))
                    .then(setLoading(true))
                    .then(DeleteAlert()),
              },
            ]}
            header="Warning"
            isOpen={isOpen}
            onClose={() => setIsOpen(false)}
            closeOnEscKey={true}
            closeOnClickOutside={false}
            variant="dialog"
          >
            <Text>Do you really want to delete order with id #{id} ?</Text>
          </Modal>
        </>
      );
    } else {
      return <div>Order Deleted</div>;
    }
  }

  function UpdateButton(id, status, is_deleted) {
    const [isOpen, setIsOpen] = useState(false);

    if (status === "Cancelled" || status === "Completed" || is_deleted) {
      return <div></div>;
    } else {
      return (
        <>
          <Button onClick={() => setIsOpen(true)} actionType="destructive">
            Cancel
          </Button>

          <Modal
            actions={[
              {
                text: "Cancel",
                variant: "subtle",
                onClick: () => setIsOpen(false),
              },
              {
                text: "Delete",
                onClick: () =>
                  orderUpdate(id)
                    .then(setIsOpen(false))
                    .then(setLoading(true))
                    .then(UpdateAlert()),
              },
            ]}
            header="Warning"
            isOpen={isOpen}
            onClose={() => setIsOpen(false)}
            closeOnEscKey={true}
            closeOnClickOutside={false}
            variant="dialog"
          >
            <Text>Are you sure you want to Cancel this order?</Text>
          </Modal>
        </>
      );
    }
  }

  const columns = [
    { header: "Order Id", hash: "id", render: ({ id }) => id },
    {
      header: "Billing Name",
      hash: "billing_address",
      render: ({ billing_address }) =>
        `${billing_address.first_name} ${billing_address.last_name}`,
    },
    {
      header: "Order Total",
      hash: "total_tax",
      render: ({ total_tax }) => total_tax,
    },
    {
      header: "Order Status",
      hash: "custom_status",
      render: ({ status, is_deleted }) => orderStatus(status, is_deleted),
    },
    {
      header: "",
      hash: "stock",
      render: ({ id, status, is_deleted }) =>
        UpdateButton(id, status, is_deleted),
    },
    {
      header: "",
      hash: "stockmm",
      render: ({ id, is_deleted }) => DeleteButton(id, is_deleted),
    },
  ];

  const onItemsPerPageChange = (newRange) => {
    setCurrentPage(1);
    setItemsPerPage(newRange);
  };

  useEffect(() => {
    getList()
      .then((items) => {
        setList(items);
        const maxItems = currentPage * itemsPerPage;
        const lastItem = Math.min(maxItems, items.length);
        const firstItem = Math.max(0, maxItems - itemsPerPage);
        setCurrentItems(items.slice(firstItem, lastItem));
      })
      .then(() => setLoading(false));
  }, [currentPage, itemsPerPage, loading]);

  return (
    <>
      <AlertsManager manager={alertsManager} />
      {loading ? (
        <Loader />
      ) : (
        <Panel header="Orders ">
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
        </Panel>
      )}
    </>
  );
}

export default OrderList;
