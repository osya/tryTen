"use strict";
const path = require("path");
const webpack = require("webpack");
const BundleTracker = require("webpack-bundle-tracker");
const ExtractTextPlugin = require("extract-text-webpack-plugin");
const rootAssetPath = path.join(__dirname, "static");

(function (extractCss, webpack2) {
    module.exports = (env) => {
        const isDevBuild = !(env && env.prod);
        return {
            entry: {
                main: [
                    "jquery", // jQuery is required by taggit-selectize
                    "bootstrap",
                    "bootstrap/dist/css/bootstrap.css",
                    path.join(rootAssetPath, "css", "main.css"),
                    path.join(rootAssetPath, "css", "theme.css"),
                    path.join(rootAssetPath, "img", "background.png")
                ],
                "selectize": [path.join(rootAssetPath, "css", "taggit_selectize", "css", "selectize.bootstrap3.css")]
            },
            output: {
                path: path.join(rootAssetPath, "static"),
                publicPath: "/static/",
                filename: "[name].[hash].js",
                library: "[name]_[hash]"
            },
            resolve: {extensions: [".js", ".css"]},
            module: {
                rules: [
                    {
                        test: require.resolve("jquery"),
                        use: [{
                            loader: "expose-loader",
                            options: "$"
                        }]
                    },
                    {
                        test: /\.css(\?|$)/,
                        use: extractCss.extract({use: [
                            isDevBuild ? "css-loader" : "css-loader?minimize", "postcss-loader"
                        ]})
                    },
                    {test: /\.(png|woff|woff2|eot|ttf|svg)(\?|$)/, use: "url-loader?limit=100000"}
                ]
            },
            stats: {modules: false},
            plugins: [
                new webpack2.ProvidePlugin({jQuery: "jquery"}), // Maps these identifiers to the jQuery package (because Bootstrap expects it to be a global variable)
                extractCss,
                new BundleTracker({filename: path.join("static", "manifest.json")})
            ].concat(isDevBuild ? [] : [new webpack2.optimize.UglifyJsPlugin()])
        };
    };
}(new ExtractTextPlugin("[name].[chunkhash].css"), webpack));
