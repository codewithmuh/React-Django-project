import React from "react";
import { Flex, ProgressCircle } from "@bigcommerce/big-design";

// Loader Genration
export default class Loader extends React.Component {
  render() {
    return (
      <div>
        <Flex justifyContent="center" style={{ marginTop: "35vh" }}>
          <ProgressCircle size="large" />
        </Flex>
      </div>
    );
  }
}
