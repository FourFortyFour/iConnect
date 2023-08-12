<script>
  import { enhance } from "$app/forms";
  import { writable } from "svelte/store";
  import NumberSelect from "../../components/NumberSelect.svelte";

  export let data;
  const priceVal = writable(data.product.price);
</script>

<div class="page">
  <!-- <Spacer /> -->
  <aside />
  <main class="content-holder">
    <div class="product-img-holder">
      <div class="img-containment">
        <img class="product-img" src="/imgs/google_rev.png" alt="" />
      </div>
    </div>
    <form action="?/pay" method="post" use:enhance>
      <h1 style="margin-bottom: 1vh;">{data.product.name}</h1>
      <div class="price-select">
        <NumberSelect name="quantity" price={priceVal} />
        <h2 class="price">AED {$priceVal}</h2>
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
      <input
        class="URL"
        name="companyURL"
        placeholder="https://www.yourcompany.com or just your company's name"
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
    transition: opacity 0.5s ease-in-out;
  }

  .product-img-holder {
    display: flex;
    /* align-items: end; */
    flex-direction: column;
    margin-right: 2%;
    /* flex: 4; */
    flex: 4;
  }

  .img-containment {
    width: 100%;
    /* overflow: hidden; */
  }

  .product-img {
    width: 100%;
    border-radius: 25px;
    box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
    /* object-fit: cover; */
  }

  .email,
  .URL {
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
  @media (max-width: 768px) {
    .img-containment {
      width: 100%;
      margin-bottom: 4%;
    }

    .product-img-holder {
      align-items: center;
    }

    .content-holder {
      flex-direction: column;
      margin-top: 4vh;
    }

    h1 {
      text-align: center;
    }

    aside {
      flex: 0.5;
    }
  }
</style>
