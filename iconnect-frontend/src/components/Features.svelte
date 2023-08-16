<section class="outer">
  <div class="inner">
    <div class="ftr">
      <img src="/imgs/trophy.webp" alt="trophy" />
      <p>Reach The Top</p>
    </div>
    <div class="ftr">
      <img src="/imgs/race.webp" alt="2 people racing" />
      <p>Get Fast Reviews</p>
    </div>
    <div class="ftr">
      <img src="/imgs/rocket.webp" alt="rocket" />
      <p>Boost your Engagement</p>
    </div>
    <div class="ftr">
      <img src="/imgs/groupy.webp" alt="a group of people" />
      <p>Convenient to Customers</p>
    </div>
  </div>
</section>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Cabin+Condensed&display=swap");

  * {
    font-family: "Cabin Condensed", sans-serif;
  }
  .outer {
    background-color: white;
    padding: 4% 0%;
  }
  .inner {
    display: flex;
    justify-content: space-around;
    align-items: center;
  }

  .ftr {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  img {
    border-radius: 100%;
    width: 45%;
  }

  p {
    font-size: 1.5rem;
    text-align: center;
  }

  @media (max-width: 425px) {
    .outer {
      padding: 4% 4%;
    }
    .inner {
      flex-wrap: wrap;
    }

    .ftr {
      flex-basis: 50%;
    }

    p {
      font-size: 1.25rem;
    }
  }
</style>
