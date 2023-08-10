<section class="outer">
  <section class="inner">
    <div class="img_part">
      <img src="/imgs/google_rev.png" alt="" />
      <a href="/order" class="get_button">Get Yours Today</a>
    </div>
    <div class="txt_part">
        <div class="alone top"></div>
        <div class="mid">
            <div class="left"></div>
            <p>
                Google Review NFC Cards 
            Unlock the power of instant feedback! Tap and review made easy. Purchase our NFC cards and make it effortless for your customers to leave a Google review. Quick, convenient, and hassle-free. Elevate your business reputation today!
            </p>
            <div class="right"></div>
        </div>
        <div class="alone btm"></div>
    </div>
  </section>
</section>

<style>
    @import url("https://fonts.googleapis.com/css2?family=Cabin+Condensed&display=swap");

    * {
    font-family: "Cabin Condensed", sans-serif;
    }
  .outer {
    padding: 4%;
    background-color: white;
  }

  .inner {
    background-color: black;
    border-radius: 50px;
    display: flex;
    padding: 2%;
    align-items: center;
    justify-content: space-around;
  }

  .img_part {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  a {
    background-color: white;
    text-align: center;
    padding: 20px 30px;
    border-radius: 25px;
    width: 50%;
    color: black;
    text-decoration: none;
    border: 5px solid rgb(255, 204, 0);
  }

  .txt_part {
    display: grid;
    align-items: center;
    justify-content: center;
  }

  .alone {
    height: 0.75vh;
    margin: 0% 7%;
    border-radius: 25px;
  }

  .top {
    background: #DA4638;
  }

  .btm {
    background: #5577AA;

  }

  .mid {
    display: flex;

  }

  .left, .right {
    width: 0.75vw;
    background-color: #DA4638;
    margin: 3% 0%;
  }

  .left {
    background: #369F52;
  }

  .right {
    background: #EEB61D;

  }

  p {
    padding: 2%;
    color: white;
    font-size: 2.75rem;
    text-align: center;
  }

  @media (min-width: 769px) and (max-width: 1024px) {
    p {
        font-size: 1.75rem;
    }

    img {
        width: 20vw;
    }

    a {
        border-width: 4px;
        padding: 4% 6%;
    }

  }

  @media (max-width: 768px) {
    .inner {
        flex-direction: column;
    }

    p {
        font-size: 1rem;
    }

    .img_part {
        margin-bottom: 2vh;
    }

    .left, .right {
        display: none;
    }

    img {
        width: 50%;
    }

    a {
        padding: 2% 2%;
        border: none;
    }
  }
</style>
