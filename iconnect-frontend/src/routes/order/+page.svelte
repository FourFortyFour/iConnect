<script>
  import { enhance } from "$app/forms";
  import NumberSelect from "../../components/NumberSelect.svelte";
  import Spacer from "../../components/LandingPageAssests/Spacer.svelte";
  export let data;

  // console.log(data.product);
</script>

<div class="page">
  <!-- <Spacer /> -->
  <aside />
  <main class="content-holder">
    <div class="product-img-holder">
      <div class="img-containment">
        <img class="product-img" src="/imgs/nfc_card_og.jpg" alt="" />
      </div>
    </div>
    <form action="?/pay" method="post" use:enhance>
      <h1 style="margin-bottom: 1vh;">{data.product.name}</h1>
      <div class="price-select">
        <NumberSelect name="quantity" />
        <h2 class="price">AED {data.product.price}</h2>
      </div>
      <h3>Description</h3>
      <p>{data.product.description}</p>
      <h3>Features</h3>
      <ul class="features">
        {#each data.product.features as feature}
          <li>{feature}</li>
        {/each}
      </ul>
      <input
        class="email"
        type="email"
        name="email"
        placeholder="any@email.com"
        required
      />

      <div class="btn-holder"><button>Buy Now</button></div>
    </form>
  </main>
  <aside />
</div>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Cabin+Condensed&display=swap");

  * {
    font-family: "Cabin Condensed", sans-serif;
    margin: 0;
  }
  .page {
    display: flex;
  }
  .content-holder {
    display: flex;
    flex: 4;
    align-items: start;
    /* justify-content: center; */
    margin-top: 3%;
  }

  form {
    display: flex;
    flex-direction: column;
    margin-left: 2%;
    flex: 4;
    /* align-items: center; */
  }

  form > * {
    margin-bottom: 2vh;
  }

  .price-select {
    display: flex;
    justify-content: space-between;
  }

  .price {
    text-align: right;
  }

  .product-img-holder {
    display: flex;
    align-items: end;
    flex-direction: column;
    margin-right: 2%;
    /* flex: 4; */
    flex: 4;
  }

  .img-containment {
    width: 70%;
    /* overflow: hidden; */
  }

  .product-img {
    width: 100%;
    object-fit: cover;
  }

  .email {
    font-size: 18px;
    border-radius: 25px;
    /* width: 100%; */
    border: 0.05px solid black;
    padding: 2%;
  }
  aside {
    flex: 1;
  }

  .btn-holder {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  button {
    background-color: #444444be;
    transition: all 250ms ease-in-out 0s;
    border: none;
    padding: 2%;
    border-radius: 52px;
    color: white;
    font-size: 18px;
    width: 25%;
  }

  button:hover {
    background-color: #444444;
  }
</style>
