<section class="about">
  <!-- <div class="break"></div> -->
  <div class="container">
    <h1 class="aboutus">ABOUT US</h1>
    <ul class="p4">
      <li>
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rem voluptatem
        ad facere et, provident vel rerum fugiat quo iusto laborum culpa facilis
        fuga tempore adipisci voluptas, architecto ipsam velit. Omnis?
      </li>
      <li>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet amet
        dolor ab placeat facere quos modi in necessitatibus officia libero
        commodi natus, praesentium corporis totam perferendis quasi laboriosam
        veniam velit?
      </li>
      <li>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel laborum
        illum assumenda deleniti sed qui dolore commodi ad cumque corporis,
        repellat, quos asperiores ullam provident quae voluptatem, iste ea quo.
      </li>
    </ul>
  </div>
  <!-- <div class="container2">
    <img
      class="statue"
      src="/imgs/card_statue.png"
      alt="statue holding a card"
    />
  </div> -->
  <!-- <div class="statue"> -->
  <img class="statue" src="/imgs/card_statue.png" alt="" />
  <!-- </div> -->
</section>

<style>
  .about {
    /* position: absolute; */

    /* display: grid;
    grid-template-rows: repeat(60, 2vh);
    grid-template-columns: repeat(50, 2vw); */

    background-color: #ffffff;
    display: flex;
    flex-direction: row;
    /* flex-wrap: wrap; */
    padding: 0 0 96px 40px;
    z-index: 3;
    justify-content: space-between;
  }

  .container {
    display: flex;
    width: 40vw;
    flex-direction: column;
    flex-wrap: wrap;
  }

  .aboutus {
    font-family: "Cabin Condensed";
    font-weight: 700;
    font-size: 3vw;
    letter-spacing: 10px;
    color: #444444;
  }

  .p4 {
    font-family: "Cabin Condensed";
    font-weight: 600;
    font-size: 2vw;
    letter-spacing: normal;
    color: #444444;
    list-style: none;
    list-style-type: none;
    text-decoration: none;

    margin: 0;
    padding: 0;

    overflow-y: hidden;
  }

  .p4 > * {
    margin-bottom: 2%;
  }

  .statue {
    /* width: 40vw; */
    /* height: auto; */
    width: 55%;
    background-image: url(/svgs/statuebg.svg);
    z-index: 1;
    overflow-x: hidden;
  }
  @media (max-width: 600px) {
    .about {
      flex-direction: column;
      justify-content: center;
      padding: 0%;
    }

    .container,
    .statue {
      width: 100%;
    }

    .aboutus {
      font-size: 5vw;
      text-align: center;
    }
    .p4 {
      font-size: 4vw;
      padding: 4%;
    }
  }
</style>
