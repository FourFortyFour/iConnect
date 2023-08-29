<script>
  import Spacer from "../../components/LandingPageAssests/Spacer.svelte";
</script>

<svelte:head>
  <title>iConnect - Contact Us</title>
</svelte:head>

<main>
  <Spacer />
  <div class="contact_content">
    <div class="contact-header">
      <h1>CONTACT US</h1>
      <!-- <img class="contactimg" src="/imgs/icon-contact.png" alt="" /> -->
    </div>
    <section>
      <form action="" method="post">
        <label for="name">
          <input type="text" name="name" placeholder="Enter your name" />
        </label>
        <label for="email">
          <input
            type="email"
            name="email"
            placeholder="email@mail.com"
            required
          />
        </label>
        <label for="phonenum">
          <input
            type="number"
            name="phonenum"
            placeholder="+971501234567"
            required
          />
        </label>
        <label for="msg">
          <textarea
            name="msg"
            id="user-message"
            cols="30"
            rows="10"
            placeholder="Message"
            required
          />
        </label>
        <div class="btn_row"><button>Send</button></div>
      </form>
    </section>
  </div>
</main>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Cabin+Condensed&display=swap");

  * {
    font-family: "Cabin Condensed", sans-serif;
  }

  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-bottom: 6%;
    background-image: url(/imgs/bck_ground.jpeg);
    background-repeat: no-repeat;
    background-size: cover;
  }

  .contact_content {
    margin: 2% 0;
    width: 50%;
    background-color: rgba(255, 255, 255, 0.8);
    border-radius: 25px;
  }

  section {
    display: flex;
    flex-direction: column;
    align-items: center;
    /* width: 100%; */
  }

  section > * {
    padding: 2%;
  }

  form {
    display: flex;
    flex-direction: column;
    flex: 1;
    align-items: center;
    width: 65%;
  }

  .contact-header {
    margin-top: 1em;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  /* .contactimg {
    width: 5vw;
  } */

  label {
    /* width: 60vw; */
    width: 100%;
    margin-bottom: 2vh;
  }

  input {
    font-size: 18px;
    border-radius: 25px;
    width: 95%;
    border: 0.05px solid black;
    padding: 2%;
  }

  #user-message {
    font-size: 18px;
    border-radius: 25px;
    width: 95%;
    border: 0.05px solid black;
    padding: 2%;
  }

  .btn_row {
    display: flex;
    flex-direction: column;
    align-items: end;
    width: 100%;
  }

  button {
    background-color: black;
    color: white;
    border: none;
    font-size: 16px;
    padding: 1.5% 5%;
    border-radius: 25px;
  }

  @media (max-width: 768px) {
    .contact_content {
      width: 90%;
    }

    .btn_row {
      align-items: center;
    }

    form {
      padding: 1%;
      width: 85%;
    }

    button {
      padding: 3.5% 8%;
      margin-bottom: 2%;
    }
  }
</style>
