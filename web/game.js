// make constant.js file
const screenWidth = window.innerWidth;
const screenHeight = window.innerHeight;

var config = {
  type: Phaser.AUTO,
  backgroundColor: 0x000000,
  width: screenWidth,
  height: screenHeight,
  scene: [Bounce]
};

var game = new Phaser.Game(config);

const events = ["keyup", "click", "touchend"]

events.forEach(function (e) {
  document.addEventListener(e, function (event) {
    game.destroy();
    game = new Phaser.Game(config);
  });
})

