<section class="outer">
  <div class="inner">
    <div class="ftr">
      <img src="/imgs/trophy.jpeg" alt="trophy" />
      <p>Be Number One</p>
    </div>
    <div class="ftr">
      <img src="/imgs/race.jpeg" alt="2 people racing" />
      <p>Get Fast Reviews</p>
    </div>
    <div class="ftr">
      <img src="/imgs/rocket.jpeg" alt="rocket" />
      <p>Boost your Engagement</p>
    </div>
    <div class="ftr">
      <img src="/imgs/groupy.jpeg" alt="a group of people" />
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
