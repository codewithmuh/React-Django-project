const path = require('path');
const HtmlwebpackPlugin = require('html-webpack-plugin');
// const { template } = require('babel-core');
const ScriptExtHtmlWebpackPlugin = require('script-ext-html-webpack-plugin');



module.exports = {
    entry: './src/index.js',
    output:{
        path: path.join(__dirname, 'dist'),
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
            inlineSource: '.(js|css)$'
        }),
        new ScriptExtHtmlWebpackPlugin({
            inline: [/\.js$/],
        })    ]
}