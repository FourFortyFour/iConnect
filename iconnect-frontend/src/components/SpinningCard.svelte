<img
  class="card2"
  id="card2"
  src="/svgs/iconnect_card.svg"
  draggable="false"
  alt="card"
/>
<img
  class="card"
  id="card"
  src="/svgs/iconnect_card.svg"
  draggable="false"
  alt="card"
/>

<style>
  .card {
    width: 25%;
    top: 30vh;
    left: 35vw;
    right: 45vw;
    position: fixed;
    /* scale:0.5; */
    rotate: -25deg;
    /* grid-area: 6/6; */

    transition: all 0.3s ease-in-out 0s;
    user-select: none;
    cursor: pointer;
    z-index: -1;
    animation: rot 10s linear infinite;
  }

  .card2 {
    opacity: 0%;
    width: 25%;
    top: 30vh;
    left: 35vw;
    right: 45vw;
    position: fixed;
    /* width: 1079px; */
    /* height: 685px; */
    /* scale: 0.5; */
    /* grid-area: 6/6; */
    rotate: -25deg;

    transition: all 0.3s ease-in-out 0s;
    z-index: 3;
    user-select: none;
    cursor: pointer;
    animation: rot 10s linear infinite;
  }

  .card2:hover {
    width: 40%;
    left: 28vw;
    top: 27vh;

    animation-play-state: paused;
    /* scale: .7; */
  }

  #card2:hover + #card {
    width: 40%;
    left: 28vw;
    top: 27vh;

    animation-play-state: paused;
    filter: drop-shadow(0px 40px 100px rgba(110, 226, 245, 1));
    /* scale: .7; */
  }

  @keyframes rot {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }


  @media (max-width: 425px) {
    .card, .card2 {
      display: none;
    }
  }
</style>
