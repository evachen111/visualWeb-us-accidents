const { defineConfig } = require('@vue/cli-service')

const webpack = require("webpack");
const path = require("path");

module.exports = defineConfig({
  transpileDependencies: [
    'vuetify'
  ],
  lintOnSave: false, // 关闭语法检查

  // 新增的,必要
  // configureWebpack: {
  //   entry: {
  //     main: './src/main.js'
  //   },
  //   externals: {
  //     jquery: 'jQuery'
  //   }
  // }
  configureWebpack: {
    plugins: [
      new webpack.ProvidePlugin({
        $: "jquery",
        jQuery: "jquery",
        "window.jQuery": "jquery",
        "window.$": "jquery",
        Popper: ["popper.js", "default"]
      })
    ],

    // devServer:{
    //   contentBase:'./',
    //   // watchContentBase:true,
    //   historyApiFallback: true
    // },

    // resolve: {
    //   extensions: ['', '.js', '.vue'],
    //   fallback: [path.join(__dirname, '../node_modules')],
    //   alias: {
    //     'src': path.resolve(__dirname, '../src'),
    //     'assets': path.resolve(__dirname, '../src/assets'),
    //     'components': path.resolve(__dirname, '../src/components'),
    //     'jquery': path.resolve(__dirname, '../node_modules/jquery/src/jquery'),
    //     'directives': path.resolve(__dirname, '../src/directives')
    //   }
    // }

    resolve: {
      extensions: ['', '.js', '.vue'],
      alias: {
        'vue$': 'vue/dist/vue.esm.js',
        '@': path.resolve('src'),
        'assets': path.resolve(__dirname, '../src/assets'),
        'jquery': "jquery/src/jquery"
      }

    }

  }

})
