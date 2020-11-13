import React from 'react';
import {Spinner, Table} from '../components';
import {ApiService} from '../services/ApiService';

export default class List extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      isOrdersLoading: true,
      orders: {
        data: [],
        pagination: {},
      },
      tableHeaders:
        [
          {
            label: "Order ID",
            index: "id",
            callback: function(orderId) {
              return orderId;
            },
          },
          {
            label: "Billing Name",
            index: "billing_address",
            callback: function(billingAddress) {
              return `${billingAddress.first_name} ${billingAddress.last_name}`;
            },
          },
          {
            label: "Order Total",
            index: "total_inc_tax",
            callback: function(orderTotal) {
              return orderTotal;
            },
          },
          {
            label: "Order Status",
            callback: function(data) {
              let badgeClass = 'badge badge-';
              if (data.status_id === 5) {
                badgeClass += 'danger';
              } else if (data.status_id === 2 || data.status_id === 10) {
                badgeClass += 'success';
              } else {
                badgeClass += 'light';
              }

              return (
                <span className={ badgeClass }>{ data.status }</span>
              );
            },
          },
          {
            label: "Actions",
            callback: function(data) {
              if (data.status_id !== 5) {
                return (
                  <button type="button" className="btn btn-danger" onClick={(e) => this.cancelOrder(data.id, e)}>Cancel</button>
                );
              }
            }.bind(this),
          },
        ],
    };
  }

  componentWillMount() {
    this.loadOrders();
  }

  loadOrders() {
    ApiService.getOrders({
      limit: 5
    }).then(this.handleOrdersResponse.bind(this));
  }

  handleOrdersResponse(response) {
    this.setState({
      isOrdersLoading: false,
      orders: {
        data: response.data
      }
    });
  }

  cancelOrder(orderId) {
  	const newOrderData = { status_id: 5 };

    this.setState({
      isOrdersLoading: true,
    });
  	
    ApiService.updateOrder(orderId, newOrderData)
    .then(this.loadOrders.bind(this));
  }

  hasOrders() {
    return (this.state.orders.data.length > 0);
  }

  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-md-12">
            <div className="card">
                <h4 className="m-4 mb-3">Orders</h4>
                {
                    this.state.isOrdersLoading
                    ? 
                    <></>
                    : 
                <h5 className="m-4">{this.state.orders.data.length } Orders</h5>
                }

                <div className="card-body">
                  {
                    this.state.isOrdersLoading
                    ? 
                    <Spinner/>
                    :
                    this.hasOrders()
                    ? 
                    <section>
                      <Table striped bordered hover tableHeaders={this.state.tableHeaders} tableData={this.state.orders.data} />
                    </section>
                    : 
                    <section>
                      <div className="emptyTable">No orders exist yet!</div>
                    </section>
                  }
                </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}