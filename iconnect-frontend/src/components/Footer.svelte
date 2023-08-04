<footer>
  <li class="foot_t">2023 iConnect. All rights reserved</li>
  <img
    class="foot_logo"
    src="/logos/logo-no-background.png"
    alt="company logo"
    draggable="false"
  />
  <ul class="foot_con">
    <li class="foot_t2">TERMS OF USE</li>
    <li class="foot_t3">PRIVACY POLICY</li>
  </ul>
</footer>

<style>
  footer {
    width: 100vw;
    height: 100px;
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
  }

  .foot_t,
  .foot_t2,
  .foot_t3 {
    color: #ffffff;
    font-family: "Cabin Condensed";
    font-size: 20px;
    font-weight: 500;
    letter-spacing: 2px;
    text-decoration: none;
    list-style: none;
  }

  .foot_t {
    margin-left: 20px;
  }

  .foot_logo {
    width: 5%;
  }

  .foot_t2,
  .foot_t3 {
    cursor: pointer;

    padding: 20px;
  }
</style>
