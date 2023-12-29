document.addEventListener("DOMContentLoaded", function() {
    var cropImage = document.getElementById("cropImage");
    var result = resultValue;
    console.log("Result:", result);
    var cropImageMap = {
        'rice': 'rice.jpg',
        'maize': 'maize.jpg',
        'chickpea': 'chickpea.jpg',
        'kidneybeans': 'kidneybeans.jpg',
        'pigeonpeas': 'pigeonpeas.jpg',
        'mothbeans': 'mothbeans.jpg',
        'mungbean': 'mungbean.jpg',
        'blackgram': 'blackgram.jpg',
        'lentil': 'lentil.jpg',
        'pomegranate': 'pomegranate.jpg',
        'banana': 'banana.jpg',
        'mango': 'mango.jpg',
        'grapes': 'grapes.jpg',
        'watermelon': 'watermelon.jpg',
        'muskmelon': 'muskmelon.jpg',
        'apple': 'apple.jpg',
        'orange': 'orange.jpg',
        'papaya': 'papaya.jpg',
        'coconut': 'coconut.jpg',
        'cotton': 'cotton.jpg',
        'jute': 'jute.jpg',
        'coffee': 'coffee.jpg'
    };
    var defaultImage = 'default.jpg';

    if (cropImageMap.hasOwnProperty(result)) {
        cropImage.src = "../static/crops/" + cropImageMap[result];
    } else {
        cropImage.src = "../static/crops/" + defaultImage;
    }
});
