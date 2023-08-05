<svg
  class="spacer some"
  viewBox="0 0 1920 1080"
  fill="none"
  xmlns="http://www.w3.org/2000/svg"
>
  <g id="bg">
    <path
      class="blue"
      id="Rectangle 49"
      d="M1920 405H1914.32C1663.58 405 1442.62 240.294 1371 0.000195861L1920 0.000195861V405Z"
      fill-opacity="0.57"
    />
    <circle
      id="Ellipse 14"
      cx="586.09"
      cy="387.933"
      r="209.5"
      transform="rotate(-166.31 586.09 387.933)"
      fill-opacity="0.8"
    />
    <path
      class="blue"
      id="Rectangle 46"
      d="M0 675C241.418 675 453.502 835.248 519.446 1067.48L523 1080H0V675Z"
      fill-opacity="0.57"
    />
    <circle
      class="blue"
      id="Ellipse 15"
      cx="597.836"
      cy="605.905"
      r="246.5"
      transform="rotate(-166.31 597.836 605.905)"
      fill-opacity="0.42"
    />
    <circle
      class="purple"
      id="Ellipse 12"
      cx="1084.17"
      cy="673.427"
      r="209"
      transform="rotate(-166.31 1084.17 673.427)"
      fill-opacity="0.4"
    />
    <path
      class="purple"
      id="Rectangle 47"
      d="M1515 1080V1074.33C1515 823.584 1679.71 602.624 1920 531V1080H1515Z"
      fill-opacity="0.35"
    />
    <circle
      class="purple"
      id="Ellipse 17"
      cx="996.383"
      cy="353.563"
      r="310"
      transform="rotate(-166.31 996.383 353.563)"
      fill-opacity="0.35"
    />
    <path
      class="purple"
      id="Ellipse 19"
      d="M1311 1080.5C1311 1001.77 1295.49 923.816 1265.37 851.082C1235.24 778.347 1191.08 712.258 1135.41 656.59C1079.74 600.921 1013.65 556.762 940.919 526.634C868.184 496.507 790.227 481 711.5 481C632.773 481 554.816 496.507 482.081 526.634C409.347 556.762 343.258 600.921 287.589 656.59C231.921 712.258 187.762 778.347 157.634 851.082C127.507 923.816 112 1001.77 112 1080.5L711.5 1080.5H1311Z"
      fill-opacity="0.35"
    />
    <circle
      class="blue"
      id="Ellipse 18"
      cx="824.383"
      cy="438.385"
      r="167.5"
      transform="rotate(-166.31 824.383 438.385)"
      fill-opacity="0.84"
    />
    <path
      class="blue"
      id="Ellipse 20"
      d="M1652 1080.5C1652 955.716 1602.43 836.042 1514.19 747.807C1425.96 659.571 1306.28 610 1181.5 610C1056.72 610 937.042 659.571 848.806 747.806C760.57 836.042 711 955.716 711 1080.5L1181.5 1080.5H1652Z"
      fill-opacity="0.86"
    />
    <path
      class="blue"
      id="Ellipse 21"
      d="M1270.44 0C1200.61 243.118 976.576 421 711 421C445.424 421 221.394 243.118 151.556 0H1270.44Z"
      fill-opacity="0.73"
    />
    <path
      class="purple"
      id="Rectangle 48"
      d="M630.999 0V9.30359C630.999 400.005 374.398 744.32 -0.00147903 856L-0.00147903 0L630.999 0Z"
      fill-opacity="0.45"
    />
    <path
      class="blue"
      id="Ellipse 21_2"
      d="M382 373.5C382 538.909 247.909 673 82.4999 673C53.8853 673 26.208 668.987 0 661.493V85.5065C26.208 78.0129 53.8853 74 82.4999 74C247.909 74 382 208.091 382 373.5Z"
      fill-opacity="0.73"
    />
    <path
      class="purple"
      id="Ellipse 22"
      d="M1090 -0.000143848L1730 1.77672e-05C1730 161 1561 334 1409 331.5C1257 329 1090 215.5 1090 -0.000143848Z"
      fill-opacity="0.68"
    />
    <path
      class="purple"
      id="Ellipse 23"
      d="M1179.57 371.331C1232.35 154.652 1450.79 21.7881 1667.47 74.5702C1777.92 101.475 1866.59 171.425 1920 262.244L1920 671.768C1832.05 821.339 1653.6 902.414 1476.33 859.232C1259.65 806.45 1126.79 588.009 1179.57 371.331Z"
      fill-opacity="0.35"
    />
  </g>
</svg>

<style>
  .spacer {
    height: 100vh;
    width: 100vw;
    scale: 2.5;

    background-repeat: repeat-x;
    background-position: center;
    background-size: cover;

    z-index: -1;
    overflow: hidden;
  }
  .purple,
  .blue {
    animation: opac 2s ease-in-out alternate-reverse infinite alternate linear;
  }

  .blue {
    fill: #6ee2f5;
    animation: bepur 3s ease-in-out alternate infinite;
  }

  .purple {
    fill: #8c1cff;
    animation: beblue 3s ease-in-out alternate infinite;
  }

  .some {
    position: fixed;
  }

  @keyframes bepur {
    0% {
      fill: #6ee2f5;
    }
    100% {
      fill: #8c1cff;
    }
  }

  @keyframes beblue {
    0% {
      fill: #8c1cff;
    }
    100% {
      fill: #6ee2f5;
    }
  }

  @keyframes opac {
    0% {
      fill-opacity: 0%;
    }
    100% {
      fill-opacity: 80%;
    }
  }

</style>
