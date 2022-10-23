(function () {

    var canvas = document.getElementById('canvas');
    canvas.width = 960;
    canvas.height = 540;

    // 中央にマスクをかけるための値を変数にいれておく
    var centerX = canvas.width / 2;
    var centerY = canvas.height / 2;

    var context = canvas.getContext('2d');

    var bgImg = new Image();
    bgImg.onload = function () {
        context.globalCompositeOperation = 'source-over';
        context.drawImage(bgImg, 0, 0, canvas.width, canvas.height);
        //drawMask();
    };
    bgImg.src = './test.jpg';  // flaskの設定に合わせて変更

    var drawMask = function () {
        // globalCompositeOperation に destination-in を設定
        context.globalCompositeOperation = 'destination-in';
        var size = 200;
        var half = size / 2;
        // 矩形を描画
        //context.fillRect(centerX - half, centerY - half, size, size);
        context.fillRect(0, 0, centerX, canvas.height)  //右半分をマスク
    };

})();