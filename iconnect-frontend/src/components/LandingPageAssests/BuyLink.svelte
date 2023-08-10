<a href="/order" class="buy">BUY NOW</a>

<style>
  .buy {
    width: 20vw;
    max-width: 500px;
    height: auto;
    padding: 20px;

    letter-spacing: 5px;
    font-size: 200%;
    font-family: "Cabin Condensed";
    font-weight: 300;
    color: #ffffff;

    background-color: #444444;

    border: none;
    /* border: 10px solid #ff0000; */
    /* border-image: linear-gradient(90deg, rgba(140,28,255,1) 0%, rgba(110,226,245,1) 100%); */
    /* border-image-slice: 1; */
    border-radius: 80px;

    grid-area: 41/35/43/48;

    user-select: none;
    z-index: 3;
    cursor: pointer;
    text-decoration: none;
    display: flex;
    text-align: center;
    align-items: center;
    justify-content: center;
  }

  .buy:hover {
    font-weight: 700;
    letter-spacing: 8px;

    transition: all 1s ease-in-out;

    background: rgb(140, 28, 255);
    background: linear-gradient(
      90deg,
      rgba(140, 28, 255, 1) 0%,
      rgba(110, 226, 245, 1) 100%
    );
  }
  @media (max-width: 768px) {
    .buy {
      width: 40vw;
      padding: 20px 25px;
      /* height: 10vh; */
      font-size: 100%;
      /* border-radius: 40px; */
      grid-area: 41/25/43/55;
      margin-bottom: 2%;
    }
  }
</style>
