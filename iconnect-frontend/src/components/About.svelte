<section class="about">
  <!-- <div class="break"></div> -->
  <div class="container">
    <div class="gradient" />
    <h1 class="aboutus">ABOUT US</h1>
    <ul class="p4">
      <li>
        Welcome to iConnect, your gateway to seamless business interactions!
        Established with a fresh perspective in 2023, we're dedicated to
        empowering businesses of all sizes with innovative NFC card solutions.
      </li>
      <li>
        At iConnect, we recognize the pivotal role that technology plays in
        modern business endeavors. Our NFC cards redefine customer engagement by
        effortlessly merging the digital and physical worlds.
      </li>
      <li>
        Whether you're looking to enhance your advertising strategies, leave a
        lasting impression with your business card, or amplify your online
        presence with authentic Google reviews, iConnect's NFC cards are the
        answer.
      </li>
      <li>
        Our mission revolves around enabling businesses to effortlessly connect
        with their audience and unlock new dimensions of growth. We're not just
        about cards we're about creating meaningful connections that foster
        loyalty and success.
      </li>
      <li>
        With a keen focus on simplicity and efficiency, we've designed our NFC
        cards to be a game-changer for businesses across industries. From local
        startups to established enterprises, iConnect is your partner in taking
        your business to the next level.
      </li>
      <li class="last">
        Join us in embracing the future of business interaction. Elevate your
        advertising, networking, and customer feedback with iConnect NFC cards.
        Your success story starts here.
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
  <img class="statue" src="/imgs/card_statue.webp" alt="" />
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
    font-size: 3rem;
    letter-spacing: 10px;
    color: #444444;
  }

  .p4 {
    font-family: "Cabin Condensed";
    font-weight: 600;
    font-size: 2rem;
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

  .last {
    font-size: 2.25rem;
  }
  @media (max-width: 600px) {
    .about {
      flex-direction: column;
      justify-content: center;
      padding: 0%;
      width: 100vw;
      background-image: url(/svgs/statuebg.svg);
    }

    .container,
    .statue {
      width: 100vw;
      background-image: none;
    }

    .aboutus {
      font-size: 5vw;
      text-align: center;
    }
    .p4 {
      font-size: 4vw;
      padding: 4%;
      text-align: center;
    }

    .gradient {
      height: 2vh;
      background: linear-gradient(105.12deg, #8c1cff -11.69%, #6ee2f5 86.28%),
        linear-gradient(0deg, #ffffff, #ffffff);
    }

    .last {
      font-size: 1.25rem;
    }
  }
</style>
