import { Panel, Text, Box, Grid } from "@bigcommerce/big-design";
import { useState, useEffect } from "react";
import Loader from "./loader";

store_hash = "4zjutairi8";

// API Get Request to store
function getStore() {
  return fetch("/bc-api/v2/store/?store_hash=${store_hash}").then((store) =>
    store.json()
  );
}
// API Get Request to store Summary
function getCatalog() {
  return fetch(
    "/bc-api/v3/catalog/summary/?store_hash=${store_hash}"
  ).then((store) => store.json());
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
          header="Store Overview"
          action={{
            variant: "secondary",
            text: "View Storefront",
            onClick: () => {
              window.open(store.secure_url);
            },
          }}
        >
          <Box
            backgroundColor="white"
            border="box"
            borderRadius="normal"
            padding="medium"
          >
            <Text>Domain</Text>
            <p>{store.domain}</p>
          </Box>
        </Panel>
      )}

      {catalog.data && (
        <Panel header="Catalog Summary">
          <p>A simple overview of your catalog.</p>

          <Grid gridColumns="repeat(3, 1fr)">
            <Box
              backgroundColor="white"
              border="box"
              borderRadius="normal"
              padding="medium"
              display="inline"
            >
              <Text>VARIANT COUNT</Text>
              <p style={{ fontSize: "2rem" }}>{catalog.data.variant_count}</p>
            </Box>
            <Box
              backgroundColor="white"
              border="box"
              borderRadius="normal"
              padding="medium"
              display="inline"
            >
              <Text>INVENTORY COUNT</Text>
              <p style={{ fontSize: "2rem" }}>{catalog.data.inventory_count}</p>
            </Box>
            <Box
              backgroundColor="white"
              border="box"
              borderRadius="normal"
              padding="medium"
              display="inline"
            >
              <Text>INVENTORY VALUE</Text>
              <p style={{ fontSize: "2rem" }}>
                {catalog.currency_symbol} {catalog.data.inventory_value}
              </p>
            </Box>
          </Grid>
        </Panel>
      )}
    </>
  );
}
