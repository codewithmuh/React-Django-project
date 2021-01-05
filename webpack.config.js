const path = require('path');
const HtmlwebpackPlugin = require('html-webpack-plugin');
const { template } = require('babel-core');


module.exports = {
    entry: './src/index.js',
    output:{
        path: path.join(__dirname, 'build'),
        filename: 'bundle.js'
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader:'babel-loader'
                }
            }
            
        ]
    },
    plugins: [
        new HtmlwebpackPlugin({
            template: './src/index.html'
        })
    ]
}