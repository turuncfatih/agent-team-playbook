# Agent Team Playbook

**Gerçek bir projeye ajan ekibi nasıl tasarlanır — rol ayrımı, görev sözleşmesi, model seçimi ve tasarımda hesaba katılması gereken hatalar.**

[![check](https://github.com/turuncfatih/agent-team-playbook/actions/workflows/check.yml/badge.svg)](https://github.com/turuncfatih/agent-team-playbook/actions/workflows/check.yml)
[![licence](https://img.shields.io/badge/lisans-MIT-blue.svg)](LICENSE)

[🇬🇧 English](README.md) · 🇹🇷 Türkçe

Çoğu ajan ekibi daha ilk prompt yazılmadan başarısız olur, çünkü roller yanlış
yerlerden kesilmiştir. Bu playbook o kesimi doğru yapmanın yöntemi: ekibin
gerekli olup olmadığına nasıl karar verilir, sınırlar nereye konur, her ajan
tanımında ne bulunmak zorundadır, hangi role hangi model katmanı verilir ve
neden, bir ajan diğerine tam olarak neyi devreder.

İki tam örnek ekiple geliyor — bir **web ürün ekibi** ve bir **backend/API
ekibi** — kopyala-yapıştır hazır ajan tanımlarıyla ve her kararın gerekçesiyle;
aksi yönde verilenler dahil.

```
8 bölüm · 3 şablon · 2 örnek ekip · 12 ajan tanımı · 3 devir sözleşmesi
```

> **Kardeş repolar.** Bu repo yöntemi anlatıyor; diğerleri makineyi ve iki
> uygulanmış örneği.
> [AgentForge](https://github.com/turuncfatih/agentforge) — orkestratörün, gate'in ve bütçenin .NET ile yazılmış hali.
> [Claude Web Workflow](https://github.com/turuncfatih/claude-web-workflow) — bu yöntemin site yapımına uygulanmış hali.
> [Claude Mobile Workflow](https://github.com/turuncfatih/claude-mobile-workflow) — React Native uygulamasına uygulanmış hali.

---

## Tez

Üç iddia; buradaki her şey bunlardan türüyor.

**1. Çoğu ajan ekibi var olmamalı.** İyi tanımlanmış tek bir ajan, çoğu işte beş
ajanlık bir ekibi geçer — daha hızlı, daha ucuz ve dikiş yerlerinde daha az
bağlam kaybederek. Ekip, **belirli bir hatanın** olasılığını düşürmek için
ödediğin bir maliyettir. O hatayı adlandıramıyorsan, hiçbir şey satın almıyorsun.

**2. Roller yetkiye ve hata türüne göre kesilir, iş unvanına göre değil.**
`frontend-dev` bir roldür çünkü repoya yazma yetkisi olan tek rol odur — şirkette
frontend geliştirici çalıştığı için değil.

**3. Yetki konfigürasyondan gelir, prompt'tan asla.** "Sadece sen
bloklayabilirsin" bir ricadır. `Write` aracını vermemek bir kontroldür.

---

## Nereden başlamalı

| Durumun | Oku |
|---|---|
| Ekibe ihtiyacın var mı emin değilsin | [1. Ne zaman ekip *kurulmaz*](docs/01-when-not-to-build-a-team.md) |
| Gerektiğinden eminsin, nasıl böleceğini bilmiyorsun | [2. Projeyi rollere kesmek](docs/02-cutting-a-project-into-roles.md) |
| Şu an bir ajan tanımı yazıyorsun | [3. Ajan spesifikasyonu](docs/03-the-agent-spec.md) + [şablon](templates/AGENT.template.md) |
| Hangi modelin nereye gideceğine karar veriyorsun | [4. Model katmanı seçimi](docs/04-choosing-a-model-tier.md) |
| Kötü çıktı üreten bir ekibi çözüyorsun | [5. Devir sözleşmeleri](docs/05-handoff-contracts.md) |
| Bozuk iş yayınlayan bir ekibi çözüyorsun | [6. Yetkiler ve veto](docs/06-permissions-and-veto.md) |
| Bir şeylerin ters gittiğini seziyorsun | [7. Anti-pattern'ler](docs/07-anti-patterns.md) |
| Ekibin çalışıp çalışmadığını ölçmek istiyorsun | [8. Ekibin çalışıyor mu?](docs/08-is-your-team-working.md) |
| Sadece kopyalayacak bir ekip arıyorsun | [examples/](examples/) — ama önce 2. bölümü oku |

---

## Yöntem, tek sayfada

### Adım 1 — Bu gerçekten bir ekip mi olmalı?

Dört test. Üçten azı geçiyorsa tek ajan istiyorsun, ya da bir script.

| Test | Soru |
|---|---|
| **Artefakt** | Her rolün ürettiği ayrı artefaktı adlandırabiliyor musun? |
| **Veto** | En az bir rol *hayır* diyebiliyor mu? |
| **Paralellik** | En az iki rol birbirinin çıktısına ihtiyaç duymuyor mu? |
| **Geri alınabilirlik** | Buradaki bir hatanın geri dönüşü pahalı mı? |

### Adım 2 — Kesimler nereden geçer?

Şu hatlardan kes:

| Kes | Kesme |
|---|---|
| **Yazma yetkisi** — repoyu kim değiştirebilir | İş unvanı |
| **Yargı türü** — zevk / doğruluk / uyum | Kıdem |
| **Yakaladığı hata türü** — adlandıramıyorsan o rol süstür | Teknoloji |
| **İhtiyaç duyduğu bağlam** — çok farklıysa ayrı roller | Görev |

Hedef: **3–6 rol**, **tek yazar**, **bir ya da iki veto**.

### Adım 3 — Her rolü tanımla

On alan. Herkesin atladığı iki tanesi, en çok iş göreni:

```
Rol · Ne zaman çağrılır/çağrılmaz · Girdiler · Çıktı sözleşmesi · Araçlar
Model katmanı · Bitti tanımı · Veto · Başarısızlık ve devir · Anti-hedefler
                                      └──────── bu ikisi ────────┘
```

### Adım 4 — Katmanı seç

> **Muhakeme seviyesi, kararın geri alınabilirliğine göre seçilir — işin prestijine göre değil.**

| Katman | Buraya ait |
|---|---|
| **Yüksek** | Planlama · mimari ve sözleşme · güvenlik incelemesi · görsel tasarım |
| **Orta** | Net spesifikasyondan uygulama · içerik · testler · doğrulama |
| **Düşük** | Sınıflandırma · çıkarım · biçimlendirme · araç çıktısını raporlama |

Uygulayıcı genellikle **en üst katman değildir**. Üst tarafta net bir spesifikasyon
varsa, geri alınamaz düşünme zaten orada yapılmıştır.

### Adım 5 — Devirleri yaz

Her dikiş için dört blok: **Sabit** · **Açık** · **Yasak** · **Kabul**.
Yasak bloğu gerçek hatalardan büyür — olgun bir ekibin yara izlerini tuttuğu yer.

### Adım 6 — Ölç

| Sayı | Sağlıklı |
|---|---|
| Veto oranı | %10–30. Sıfır ise gate süstür |
| Eskalasyon oranı | %5–15. Sıfır ise kötü iş yayına çıkıyor |
| Role göre rework | Tek rolde toplanıyorsa o rolü düzelt. Dağılmışsa devirleri |
| Role göre çağrılma | Sıfıra yakınsa o rolü sil |

---

## İki örnek ekip

Aynı yöntem, farklı cevaplar — çünkü işlerin geri alınabilirlik profili farklı.
**Asıl değer bu karşıtlıkta.**

### [Web ürün ekibi](examples/web-product-team/)

`tech-lead` · `designer` · `content-writer` · `frontend-dev` · `seo-auditor` · `verifier`

```
tech-lead planlar
   ├─ designer ───────┐   (paralel)
   └─ content-writer ─┤
                      ▼
                 frontend-dev  ← tek yazar
                      ▼
        seo-auditor ──┴── verifier (VETO)
                      ▼
            kırmızı? → rework (max 2) → insan
```

### [Backend / API ekibi](examples/backend-api-team/)

`tech-lead` · `api-designer` · `implementer` · `test-engineer` · `security-reviewer` · `verifier`

```
tech-lead planlar
      ▼
api-designer  ← geri alınamaz karar sözleşmedir
      ▼
   ┌──┴───────────────┐   (paralel — ikisi de sözleşmeyi okur, birbirini asla)
   ▼                  ▼
implementer      test-engineer
   └──────┬───────────┘
          ▼
security-reviewer ──┴── verifier
   (yargı VETO'su)      (olgu VETO'su)
          ▼
   bloklandı? → rework (max 3) → insan
```

### Ne değişti, neden

| | Web ekibi | Backend ekibi | Neden |
|---|---|---|---|
| Yazar sayısı | 1 | **2**, dizinle ayrılmış | Test ve kaynak farklı artefaktlar, farklı inceleme kriterleri — ve kendi testini yazan uygulayıcı, *geçen* testler yazar, *doğru* testler değil |
| Veto sayısı | 1 (olgu) | **2** (yargı + olgu) | Yayına çıkmış bir yetkilendirme açığı bir edit'le düzeltilemez |
| En üst katman | `designer` | `api-designer` | Burada geri alınamaz olan sözleşme, görünüm değil |
| Rework sınırı | 2 | **3** | Güvenlik bulguları çoğu kez iki deneme ister; birini yayınlamanın maliyeti üçüncü turdan yüksek |

İki ekip de **bilerek oluşturulmayan rolleri** ve gerekçelerini belgeliyor.

---

## İki tür veto

Çoğu ekibin kaçırdığı ayrım — ve iki gate'in kilitlenmeden bir arada
durabilmesinin sebebi:

| | Yargı vetosu | Olgu vetosu |
|---|---|---|
| Örnek | `security-reviewer` | `verifier` |
| Dayanak | Uzmanlık | Araç çıktısı |
| Kanıt gerekir mi | **Evet, zorunlu** — atıfsız blok bir görüştür | Kendisi zaten kanıttır |
| Geçersiz kılınabilir mi | İnsan tarafından, kayda geçerek | Hayır — düzelt |
| Yanlış ayarlanırsa | Her şeyi bloklar ya da hiçbir şeyi | Kararsız çalışır, sonra yok sayılır |

Üçüncü bir veto ekibi kilitler. Her iki örnek de hangi role veto **verilmediğini**
ve nedenini yazıyor.

---

## Şablonlar

| Şablon | Ne için |
|---|---|
| [`AGENT.template.md`](templates/AGENT.template.md) | Tek ajan tanımı — on alan, her biri için yönlendirmeyle |
| [`HANDOFF.template.md`](templates/HANDOFF.template.md) | Tek dikiş — Sabit / Açık / Yasak / Kabul |
| [`TEAM.template.md`](templates/TEAM.template.md) | Tüm ekip tek sayfada, dört gerekçe testiyle |

Ajan tanımları Claude Code'un `.claude/agents/*.md` frontmatter formatını
kullanıyor, yani örnekler doğrudan bir projeye düşüyor. Yöntem çalışma
ortamından bağımsız — sadece frontmatter'a özgü.

---

## On üç anti-pattern

Her biri [7. bölümde](docs/07-anti-patterns.md) belirti, sebep ve çözümüyle.

| | | |
|---|---|---|
| Komite | Doğrulayıcı yok | Yazan kendini onaylıyor |
| Herkeste her araç | Süs veto | Sonsuz döngü |
| "Yardımcı ol" | Bağlam tıkması | Script olması gereken ajan |
| Sessiz retry | İşi kendi yapan orkestratör | **İstenmeyen artefakt** |
| Bulduğun ekibi kopyalamak | | |

Şu an bir ekibi çözüyorsan en hızlı üç kontrol:
**doğrulayıcı var mı?** · **veto hiç ateşleniyor mu?** · **neredeyse hiç
çağrılmayan bir rol var mı?**

---

## Tek soru

Bu playbook'tan başka hiçbir şey kalmasın, bu kalsın:

> **Ekibin en son yanlış bir şey yayınladığında — hangi rol bunu yakalamalıydı ve neden yakalamadı?**

- *"Hiçbir rol yakalamakla yükümlü değildi"* → eksik rol
- *"O rol var ama bağlamı yoktu"* → devir sorunu
- *"O rol yakaladı ama geçersiz kılındı"* → veto sorunu

Tek soruda üç teşhis, ve her ekipte çalışır.

---

## İçerik

```
docs/
  01-when-not-to-build-a-team.md      dört test ve checklist testi
  02-cutting-a-project-into-roles.md  sınırlar nereden geçer
  03-the-agent-spec.md                on alan, tek tek
  04-choosing-a-model-tier.md         prestij değil, geri alınabilirlik
  05-handoff-contracts.md             Sabit / Açık / Yasak / Kabul
  06-permissions-and-veto.md          en az yetki, iki tür veto
  07-anti-patterns.md                 on üç tane, çözümleriyle
  08-is-your-team-working.md          beş sayı
templates/
  AGENT.template.md · HANDOFF.template.md · TEAM.template.md
examples/
  web-product-team/     6 ajan, 2 devir, tam gerekçe
  backend-api-team/     6 ajan, 1 devir, tam gerekçe
```

> Bölüm içerikleri ve ajan tanımları İngilizce yazıldı — kopyalanabilir olmaları
> ve uluslararası okuyucuya açık kalmaları için.

---

**Lisans** · MIT — şablonları kopyala, ekipleri kopyala, yöntemi kopyala.
