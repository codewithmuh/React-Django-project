import React from 'react';

export class Table extends React.Component {
  constructor(props) {
    super(props);
  }



  getTableRow(data, index) {
    return (
      <tr key={index}>
      {this.props.tableHeaders.map(function(header, index) {
        let value = data;
        if (header.index) {
          value = data[header.index];
        }

        if (header.callback) {
          value = header.callback(value);
        }

        return <td key={index}>{value}</td>
      })}
      </tr>
    );
  }

  
  

  render() {

    
    // Get current Pages
    const indexOfLastPage = this.props.currentPage * this.props.rowPerPage;
    const indexOfFirstPage = indexOfLastPage - this.props.rowPerPage;
    const paginated = this.props.tableData.slice(indexOfFirstPage, indexOfLastPage);


    return (
      <table className="table">
        <thead className="table-thead" style={{background: '#f3f3f3'}}>
          <tr>{this.props.tableHeaders.map(function(header, index) {
            return <td key={index}>{header.label}</td>;
          })}</tr>
        </thead>
        <tbody className="table-tbody">
          {paginated.map(this.getTableRow.bind(this))}
        </tbody>
      </table>
    );
  }
}