 var canvas = document.getElementById('canvas');
                canvas.width = 850;
                canvas.height = 400;
                var context = canvas.getContext('2d');
                var bgImg = new Image();
                bgImg.onload = function () {
                    context.globalCompositeOperation = 'source-over';
                    context.drawImage(bgImg, 0, 0, canvas.width, canvas.height);
                };
                bgImg.src = '../static/image/test2.jpg';  // flaskの設定に合わせて変更