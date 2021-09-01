module.exports = {
    publicPath: '/static/', //process.env.NODE_ENV === 'production' ? '/static/dist/' : 'http://localhost:8080',
    // outputDir: '../app/static/dist',
    indexPath: '../base.html',
    css: {
        requireModuleExtension: false
    },
    chainWebpack: config => {
        config.devServer
            .public('http://localhost:8080')
            .hotOnly(true)
            .headers({'Access-Control-Allow-Origin': '*'})
            .writeToDisk(true)
    }
}