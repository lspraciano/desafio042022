const gifPreloadingErlen = document.getElementById('pre-loader')
const boxGif = document.getElementById('gif-erlen')


export const startPreloading = () => {

    gifPreloadingErlen.style.display = "flex"
    boxGif.style.display = "flex"


}

export const stopPreloading = () => {

    gifPreloadingErlen.style.display = "none"
    boxGif.style.display = "none"



}

