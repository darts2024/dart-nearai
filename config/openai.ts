import OpenAI from "openai";

const auth =  {
  "account_id": "hirocoin.near",
  "signature": "N2cDrk0F/8NdsiXFBf8NWzoBpiuPEk8xTU4IYAS4+itWdW8WNFguQ8mujgEvXQGb6IHHGDbwhYjwz3RddA2bBw==",
  "public_key": "ed25519:GSawU7vtBcUCq3m9VyETsp9xzUz1L5XBf9H4JkdngfyX",
  "callback_url": "http://localhost:51738/capture",
  "nonce": "1748226368326",
  "recipient": "ai.near",
  "message": "Welcome to NEAR AI",
  "on_behalf_of": null
}


export const initializeOpenAI = (auth: any) => {
  let baseUrl = "https://api.near.ai/v1";
  return new OpenAI({
    baseURL: baseUrl,
    apiKey:  `${JSON.stringify(auth)}`,
  });
};


export const openai = initializeOpenAI(auth);