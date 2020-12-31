import { Panel, Text, Flex, H2 } from "@bigcommerce/big-design";
import { useState, useEffect } from "react";
import Loader from "./loader";

// API Get Request to store
function getStore() {
  return fetch("/bc-api/v2/store").then((store) => store.json());
}
// API Get Request to store Summary
function getCatalog() {
  return fetch("/bc-api/v3/catalog/summary").then((store) => store.json());
}

export default function Summary() {
  const [store, setStore] = useState([]);
  const [catalog, setCatalog] = useState([]);

  useEffect(() => {
    getStore().then((foo) => {
      setStore(foo);
    });

    getCatalog().then((foo) => {
      setCatalog(foo);
    });
  }, [store.id, catalog.id]);

  return (
    <>
      {store.length === 0 ? (
        <Loader />
      ) : (
        <Panel
          header="Stor Overview"
          action={{
            variant: "secondary",
            text: "View Storefront",
            onClick: () => {
              window.open(store.secure_url);
            },
          }}
        >
          <Panel>
            <Text>Domain</Text>
            {store.domain}
          </Panel>
        </Panel>
      )}

      {catalog.data && (
        <Panel header="Catalog Summary">
          <Flex justifyContent="space-between">
            <Panel>
              <Text>VARIANT COUNT</Text>
              <H2>{catalog.data.variant_count}</H2>
            </Panel>
            <Panel>
              <Text>INVENTORY COUNT</Text>
              <H2>{catalog.data.inventory_count}</H2>
            </Panel>
            <Panel>
              <Text>INVENTORY VALUE</Text>
              <H2>{catalog.data.inventory_value}</H2>
            </Panel>
          </Flex>
        </Panel>
      )}
    </>
  );
}
