export const preProcessingData = async (data) => {
    let transactionDate = data[0];
    transactionDate = transactionDate[transactionDate.length - 1].substring(0,10);
    let outputValidData = [];
    let outputInvalidDataIndex = [];

    await data.forEach((item, index) => {
        if(item.includes('') || item[item.length - 1].substring(0,10) !==  transactionDate) {
            outputInvalidDataIndex.push(index+1);
        } else {
            outputValidData.push(item);
        }
    });

    return {
        'outputValidData':outputValidData,
        'outputInvalidData': outputInvalidDataIndex
    }
}
