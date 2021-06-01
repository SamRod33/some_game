// make constant.js file
const screenWidth = 1760;
const screenHeight = 840;

var config = {
  type: Phaser.AUTO,
  backgroundColor: 0x000000,
  width: screenWidth,
  height: screenHeight,
  scene: [Bounce]
};

var game = new Phaser.Game(config);