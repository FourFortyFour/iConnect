<ul class="container1">
  <li class="p">ICONNECT,</li>
  <li class="p2">CONNECT EASIER.</li>
</ul>

<style>
  .container1 {
    grid-area: 41/1/43/51;
    width: 30vw;
    max-width: 500px;
    height: 200px;

    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    z-index: 3;
    user-select: none;
    transition: all 0.3s ease-in-out;
  }

  .p,
  .p2 {
    font-family: "Cabin Condensed";
    font-size: 3vw;
    letter-spacing: 7px;
    line-height: 100px;
    font-weight: 600;
    color: #444444;
    text-decoration: none;
    list-style: none;
    text-align: left;
    transition: all 2s ease-in-out;
  }

  .p:hover {
    color: rgba(140, 28, 255, 1);
  }

  .p2:hover {
    color: rgba(110, 226, 245, 1);
  }

  @media (max-width: 600px) {
    .container1 {
      width: 20vw;
      max-width: 300px;
      /* height: 100px; */
      /* grid-area: 41/1/43/51; */
    }

    .p,
    .p2 {
      font-size: 7vw;
      letter-spacing: 5px;
      line-height: 50px;
    }
  }
</style>
