const path = require('path')
var webpack=require('webpack')
// const webpack = require("webpack");
module.exports = {
    entry:path.join(__dirname,'./src/main.js'),
    output:{
        path:path.join(__dirname,'dist'),
        filename:'bundle.js',
        publicPath: '/',
    },

    plugins: [
        new webpack.ProvidePlugin({
            $:"jquery",
            jQuery:"jquery",
            "windows.jQuery":"jquery"
        })
    ] ,

    devServer:{
        contentBase:'./',
        watchContentBase:true,
        historyApiFallback: true
    },

    resolve: {
        extensions: ['', '.js', '.vue'],
        // fallback: [path.join(__dirname, '../node_modules')],
        // alias: {
        //     'src': path.resolve(__dirname, '../src'),
        //     'assets': path.resolve(__dirname, '../src/assets'),
        //     'components': path.resolve(__dirname, '../src/components'),
        //     'jquery': path.resolve(__dirname,  '../node_modules/jquery/src/jquery'),
        //     'directives': path.resolve(__dirname, '../src/directives')
        // }

        alias: {
            'vue$': 'vue/dist/vue.esm.js',
            '@': path.resolve('src'),
            'assets': path.resolve(__dirname, '../src/assets'),
            'jquery': "jquery/src/jquery"
        }

    }
}
