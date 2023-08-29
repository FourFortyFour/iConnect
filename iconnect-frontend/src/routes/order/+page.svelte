<script>
  import { enhance } from "$app/forms";
  import { writable } from "svelte/store";
  import NumberSelect from "../../components/NumberSelect.svelte";
  import Spacer from "../../components/LandingPageAssests/Spacer.svelte";
  import Slider from "../../components/Slider.svelte";

  export let data;
  const priceVal = writable(data.product.price);

  const urls = [
    { url: "/imgs/google_rev.webp", alt: "google review card" },
    {
      url: "/imgs/product_1.webp",
      alt: "person holding up google review card",
    },
    {
      url: "/imgs/product_2.webp",
      alt: "person holding up google review card",
    },
    {
      url: "/imgs/product_3.webp",
      alt: "person holding up google review card",
    },
  ];
</script>

<svelte:head>
  <title>iConnect - Buy Now</title>
</svelte:head>

<Spacer />
<div class="page">
  <!-- <aside /> -->
  <main class="content-holder">
    <div class="product-img-holder">
      <div class="img-containment">
        <Slider {urls} />
      </div>
    </div>
    <form action="?/pay" method="post" use:enhance>
      <h1 style="margin-bottom: 1vh;">{data.product.name}</h1>
      <div class="price-select">
        <NumberSelect name="quantity" price={priceVal} />
        <h2 class="price">AED {$priceVal}</h2>
      </div>
      <h3>Description</h3>
      <p class="description">{data.product.description}</p>
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
</div>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Cabin+Condensed&display=swap");

  * {
    font-family: "Cabin Condensed", sans-serif;
    margin: 0;
  }
  .page {
    display: flex;
    align-items: center;
    justify-content: center;
    padding-bottom: 10%;
  }
  .content-holder {
    display: flex;
    /* flex: 4; */
    align-self: start;
    justify-content: center;
    margin-top: 3%;
    background-color: rgba(255, 255, 255, 0.8);
    padding: 3%;
    border-radius: 25px;
    width: 55%;
  }

  form {
    display: flex;
    flex-direction: column;
    margin-left: 2%;
    width: 40%;
    /* flex: 4; */
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
    /* flex: 4; */
  }

  .img-containment {
    width: 100%;
    display: flex;
    justify-content: flex-end;
    /* overflow: hidden; */
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
    .content-holder {
      width: 65vw;
    }
    .img-containment {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 90%;
      margin-bottom: 4%;
    }

    .product-img-holder {
      align-items: center;
      width: 100%;
    }
    .email,
    .URL {
      width: 40vw;
    }

    button {
      width: 55vw;
    }

    .content-holder {
      flex-direction: column;
      margin-top: 4vh;
      margin-bottom: 7vh;
      padding-bottom: 7vh;
    }

    h1 {
      text-align: center;
    }

    aside {
      flex: 0.5;
    }
    .description {
      width: 40vw;
    }
  }
</style>
