<footer>
  <li class="foot_t">2023 iConnect. All rights reserved</li>
  <img
    class="foot_logo"
    src="/logos/logo-no-background.webp"
    alt="company logo"
    draggable="false"
  />
  <a class="small-only" href="/gdpr">Privacy Policy</a>
  <a class="small-only" href="/tos">Terms Of Service</a>
  <ul class="foot_con">
    <li class="foot_t2"><a href="/tos">TERMS OF SERVICE</a></li>
    <li class="foot_t3"><a href="/gdpr">PRIVACY POLICY</a></li>
  </ul>
</footer>

<style>
  * {
    font-family: "Cabin Condensed", sans-serif;
  }
  a {
    text-decoration: none;
    color: white;
  }

  .small-only {
    display: none;
  }
  footer {
    width: 100%;
    /* height: 100px; */
    margin-top: 2%;
    bottom: 0;
    position: absolute;
    background-color: #444444;
    z-index: 100000;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    user-select: none;
  }

  .foot_con {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-self: flex-end;
    gap: 1rem;
  }

  .foot_t,
  .foot_t2,
  .foot_t3 {
    color: #ffffff;
    font-family: "Cabin Condensed";
    font-size: 1.2rem;
    font-weight: 500;
    letter-spacing: 2px;
    text-decoration: none;
    list-style: none;
  }

  .foot_t {
    margin-left: 20px;
  }

  .foot_logo {
    width: 5rem;
    height: auto;
  }

  .foot_t2,
  .foot_t3 {
    cursor: pointer;
    padding: 20px;
  }

  @media (max-width: 768px) {
    .small-only {
      display: contents;
    }
    footer {
      position: relative;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }

    .foot_logo {
      width: 10vw;
      padding: 2%;
      /* margin-bottom: 1rem; */
    }

    .foot_con {
      /* flex-direction: column; */
      margin-bottom: 1rem;
      gap: 0.5rem;
    }

    .foot_t,
    .foot_con {
      display: none;
    }

    .foot_t,
    .foot_t2,
    .foot_t3 {
      font-size: 1rem;
      padding: 0;
    }
  }
</style>
