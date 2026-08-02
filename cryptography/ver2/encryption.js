// この問題のアルファベットを入れてください
  const alphabet = "A";

  // この問題の得点を入れてください
  const points = [50,125];

  // 小課題ごとの対応するテストケース番号を入れてください
  const tasks = [[1],[1,2]];

  // コンテストで共通する秘密鍵を入力してください(英文字で入力、空白禁止)
  const secret = "MY_SECRET_KEY";

// 中略...

// Base64URLエンコード
  function base64urlEncode(bytes) {
    let binary = "";
    for (const b of bytes) binary += String.fromCharCode(b);

    return btoa(binary)
      .replace(/\+/g,"-")
      .replace(/\//g,"_")
      .replace(/=+$/,"");
  }

  // HMAC-SHA256
  async function hmacSHA256(message) {
    const key = await crypto.subtle.importKey(
      "raw",
      new TextEncoder().encode(secret),
      { name: "HMAC", hash: "SHA-256"},
      false,
      ["sign"]
    );

    const sig = await crypto.subtle.sign(
      "HMAC",
      key,
      new TextEncoder().encode(message)
    );

    return new Uint8Array(sig);
  }

  async function makeCode(dt,ch,P) {
    const msg = `${dt}:${ch}:${P}`;

    const payload = base64urlEncode(
      new TextEncoder().encode(msg)
    );

    const sig = base64urlEncode(
      await hmacSHA256(msg)
    );

      return payload + "." + sig;
  }
