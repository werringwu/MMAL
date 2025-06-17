# Rebuttal Response to LrXP
Thanks for responses.
## RQ1@Explain mathematical derivation  on local monents.
According to convolution theorem, MMAL (Eq.6) compares the Fourier transforms of $\mathrm{\mathbf{I}(x,y)·\mathbf{K}(x,y)}$, built from image moments (Eq.7) to encode structure. $\mathrm{\mathbf{K}(x,y)}$ breaks the conditions $\mathrm{\mathbf{I}{(x_1,y_1)}}=\mathrm{\mathbf{I}{(x_2,y_2)}}=\mathrm{\mathbf{I}{(x_3,y_3)}}$ and $\mathrm{\delta_{x_2,y_2,x_3,y_3}}=0$ between smooth and structural pixels in Eq.3, making amplitude sensitive to local structural changes and thus enhancing structural details (Tab.1).

Tab.1 Ablation study
||w/o g(z)|w/o $M^(2)$|w/o λ|w/o Amp|all
-|-|-|-|-|-
PSNR/SSIM|22.99/.91|25.91/.941|26.4/.942|25.33/.93|26.63/.944
## RQ2@Evaluate on real-world noisy.
In Tab.2 & Tab.3, MMAL outperforms the baseline (RetinexFormer).

Tab.2 Result of SID/SMID.
| |baseline|MMAL|
-|-|-
SID|24.25/.672|24.34/.673
SMID|29.15/.815|29.28/.816

Tab.3 Noise vs PSNR/SSIM (LOL v2-real).
|$\sigma^2$|0|.02|.04|.06|.1
-|-|-|-|-|-
baseline|22.80/.84|20.74/.694|18.8/.59|17.8/.522|16.29/.277
MMAL|23.21/.875|21.3/.785|19.65/.669|18.93/.582|16.96/.378

## RQ3@Compare with SOTA.
In Tab.4, RetinexFormer+MMAL surpasses recent methods.

Tab.4 Comparison with SOTA.
PSNR/SSIM|MambaLLIE'25|FourLLIE'23|WaveMamba'24|Diff-Retinex++'25|RetinexFormer+MMAL
-|-|-|-|-|-
LOLv1|-|20.53/.796|21.02/.808|24.67/.867|25.4/.872
LOLv2-syn|25.87/.94|23.14/.88|23.32/.885|26.06/.944|26.63/.944

## RQ4@Compute cost.
In Tab.5, MMAL adds minor training time and FLOPS, unchange parameters and inference time. Lightweight design will be explored in future work.

Tab.5 Compute cost(RetinexFormer,LOLv2-syn).
||Baseline|MMAL
-|-|-
Train/Infer(ms)|48.7/7.2|54.3/7.2
FLOPS(G)|15.57|15.96
Params(M)|1.61|1.61
## RQ5@Clarify "semi-local".
Semi-local refers to moment statistics computed over a window(15x15,smaller than the full image) centered at each pixel, which captures structural patterns beyond individual pixels,  enabling mid-range spatial awareness,  preserving semi-local consistency across the image while integrating into frequecy-domain information (Sec. 3.2).  The imfact in Tab.1. Visuals will be opensource repo.
## FJ@Overfitting.
Thanks for pointing out. The score of HWMNET was misreported (38.26→57.13 ), which without overfitting.


# Rebuttal Response to D8KM
Thanks for feedback.
## RQ1@Clarify design motivation and "semi-local".
Frequency-based methods excel at capturing global patterns but their amplitude components are often insensitive to spatial structural changes, leading to local detail loss (Sec. 3.1). MMAL addresses this by modulating frequency amplitudes via spatial moment statistics, preserving semi-local structures while leveraging frequency benefits. The chosen $\mathrm{g(z)}$, with derivative $\frac{1}{(2+z)^2}$, facitilates disturbances invariance and stabilizes optimization. Window-based moment introduces spatial awareness (Fig. 2). The effectiveness of this design is validated in Tab. 1.

Tab.1 Diff monotonic.
||$\log(1+z)$|$2^z$|$\frac{1}{1+\exp^{-z}}$|$\frac{1+z}{2+z}$
-|-|-|-|-
PSNR/SSIM|23.92/.922|25.63/.939|26.33/.942|26.63/.944
## RQ2@Extremely low-light with severe noise and failure case.
MMAL enhances low-light images by modulating amplitude with local intensity variations, yielding structure-aware, noise-robust enhancement. In Fig.4 (row 5,6), MMAL delivers cleaner details under heavy noise vs. baselines. Tab.2 shows improvements over RetinexFormer under increasing noise. Baseline models remain brightness discontinuities which MMAL improves structure and reduces noise and still remains a limitation. We aim to address it in future work with noise-handling modules.

Tab.2 Noise vs PSNR/SSIM (LOL v2-real).
|$\sigma^2$|0|.02|.04|.06|.1
-|-|-|-|-|-
baseline|22.80/.84|20.74/.694|18.8/.59|17.8/.522|16.29/.277
MMAL|23.21/.875|21.3/.785|19.65/.669|18.93/.582|16.96/.378
## RQ3@Computational efficiency
In Tab.3, MMAL adds minor training time and FLOPS, unchange parameters and inference time, meeting real-time application.

Tab.3 Computational efficiency(RetinexFormer).
||Baseline|MMAL
-|-|-
Train/Infer(ms)|48.7/7.2|54.3/7.2
FLOPS(G)|15.57|15.96
Params(M)|1.61|1.61
## RQ4,RQ5@Ablation study.

Tab.4. ablation confirms g(z) essential for SSIM↓, $M^(2)$ impacts both PSNR↓/SSIM↓ (detail preservation).  Visuals will in open-source repo.
||w/o g(z)|w/o $M^(2)$|w/o λ|w/o Amp|all
-|-|-|-|-|-
PSNR/SSIM|22.99/.91|25.91/.941|26.4/.942|25.33/.93|26.63/.944
## ACs@missing recent methods.

Tab.5 compares with other SOTA.
PSNR/SSIM|MambaLLIE|WaveMamba|RetinexFormer+MMAL
-|-|-|-
LOLv2-syn|25.87/.94|23.32/.885|26.63/.944

# Rebuttal Response to Um3Y
Thanks for valuable feedback.
## RQ1@Limited Novelty.
MMAL is the first to fuse spatial structure into frequency domain by using moment statistics $\mathrm{\mathbf{K}(x,y)}$ through convolution theorem (Eq.6 & 7), which hightlights semi-local structures such as large edges (Fig.2 manuscript), maintaining detailed structure while benefiting from the frequency domain’s global features. Compared to [15,47], we theoretically explain and analyze the loss of details (Sec.3.1), which can be avoided by MMAL in part under theoretical analyses. MMAL outperforms serveral SOTA methods (Tab.1,2, manuscript) and boosts performance when combined with frequency-domain methods(Tab.1).  

Tab.1 Comparison with frequency method in LOL v2-syn.
||FECNet|FECNet+MMAL|FourLLIE'23|FourLLIE+MMAL|RetinexFormer+MMAL
-|-|-|-|-|-
PSNR/SSIM|22.764/.899|23.35/.912|23.14/.88|23.54/.91|26.63/.944
## RQ2@Methodological Clarity.
The choice of $\mathrm{g(z)}=\frac{1+z}{2+z}$ facilitates invariablitiy of MMK to spatial disturbance as in Fig.2. Specifically, according to the chain rule, the $\frac{1}{(2+z)^2}$ makes values in difference map of image moments caused by spatial disturbances tend to be zero, facilitating invariablitiy to spatial disturbance in optimizating nonlinear continuous network. In Tab.1, we validated this choice against alternatives, and $\mathrm{g(z)}$ consistently achieved the best PSNR/SSIM across LLIE benchmarks. 

Tab.3 Diff monotonic.
||$\log(1+z)$|$2^z$|$\frac{1}{1+\exp^{-z}}$|$\frac{1+z}{2+z}$
-|-|-|-|-
PSNR/SSIM|23.92/.922|25.63/.939|26.33/.942|26.63/.944
## RQ3-1@Ablation study on moment order or window size.
The imfact of moment order have been analyzed (Tab.4 manuscript) and window size shown in Tab.4. 

Tab.4 Diff kernel size.
Size|7|9|11|13|15|17|19
-|-|-|-|-|-|-|-
PSNR/SSIM|25.54/.938|26.33/.938|26.1/.941|26.23/.941|26.63/.944|26.04/0.937|25.85/.94
## RQ3-2@Comparisons with Fourier-domain methods.
MMAL significantly improves baseline performance (Tab.1) and structural benefits beyond frequency priors, approaching RetinexFormer+MMAL.

# Rebuttal Response to Pudy
Thanks for valuable time and efforts.
## RQ1@Methodological Clarity & MMK functions justify.
MMAL introduces a novel structure-aware loss by modulating the frequency amplitude using local moments statistics, which encode semi-local structural patterns. MMAL uniquely bridges spatial domain statistics and frequency learning through convolution theorem. Furthermore, we mathematically analyse the loss of image details in Eq.3, where the delicate conditions of unexcepted coincident soltuions can be broken by MMK. Specifically, MMK is derived by computing moment statistics over spatial windows, forming a semi-local modulation map in Eq.7. This map scales the frequency amplitude in a structure-aware manner. The choice of $\mathrm{g(z)}=\frac{1+z}{2+z}$ facilitates invariablitiy of MMK to spatial disturbance as in Fig.2, whose superiority can also be verified by experiments as in Tab.1.

Tab.1 Diff monotonic.
||$\log(1+z)$|$2^z$|$\frac{1}{1+\exp^{-z}}$|$\frac{1+z}{2+z}$
-|-|-|-|-|
PSNR↑/SSIM↑|23.92/.922|25.63/.939|26.33/.942|26.63/.944
## RQ2@computational complexity.
Thank you for your valuable feedback. We evaluated the computational complexity of MMAL and compared it with other loss functions like FFL and LPIPS (VGG). In Tab.2, MMAL introduces a small increase in training time (54.295 ms) and FLOPs (15.958 G) compared to the baseline (RetinexFormer). However, the parameter count remains unchanged at 1.61M, and the inference time for a 256x256 image is 7.19 ms, which meets real-time requirements. 

Tab.2 Diff loss(RetinexFormer,LOLv2-syn).
||Baseline|FFL|LPIPS(VGG)|MMAL
-|-|-|-|-
PSNR↑/SSIM↑|25.67/.93|23.58/.858|26.29.932|26.63/.944
Train/Infer(ms)|48.7/7.2|49.7/7.2|55.2/7.2|54.3/7.2
FLOPS(G)|15.57|15.60|55.68|15.96
Params(M)|1.61|1.61|14.72|1.61

## Cons3@Discussion of failure cases.
In extreme low-light conditions with high noise, baseline models often exhibit brightness discontinuities. While MMAL improves structure & reduce noise, the issue remains. We aim to tackle this in future work with noise-aware modules or improved loss designs. 

## Cons4@Add discussion of related work.
In the revised manuscript, we discussed FourLLIE and other frequency-based[1-3] method, which focus on frequency-domain information, enhancing global patterns while neglecting local structure and details. These approaches often fails to capture fine image details, which are critical for effective LLIE.

[1] WaveMamba.
[2] FourLLIE.
[3] FECNet.

# Rebuttal Response to ndrB
Thanks for responses.
## RQ1@Theoretical justification of MMK.
The choice of $\mathrm{g(z)}=\frac{1+z}{2+z}$ facilitates invariablitiy of MMK to spatial disturbance as in Fig.2. According to the chain rule, the $\frac{1}{(2+z)^2}$ makes values in difference map of image moments caused by spatial disturbances smaller, facilitating invariablitiy to spatial disturbance in optimizating nonlinear continuous network. In Tab.1, we validated this choice against alternatives, and $\mathrm{g(z)}$ achieved the best performances in LOL v2-syn. 

Tab.1 Diff monotonic.
||$\log(1+z)$|$2^z$|$\frac{1}{1+\exp^{-z}}$|$\frac{1+z}{2+z}$
-|-|-|-|-|
PSNR/SSIM|23.92/.922|25.63/.939|26.33/.942|26.63/.944
## RQ2@Contributions of MMAL.
MMAL is the first to integrate moments as a loss for Low-Level Vision, opening new avenues for cross-domain learning. Traditional frequency-based method [15,47] directly manipulate amplitude or phase. MMAL innovatively combines moments  with a monotonic kernel to modulate the frequency domain, breaking the traditional boundary between spatial & frequency domains through convolution theorem, which maintains semi-local details while benefiting from frequency-domain enhancements. MMAL outperforms serveral SOTA methods (Tab.1,2, manuscript) and boosts performance when combined with frequency-domain methods(Tab.2). While mixed cross-domian networks incurs significant cost, MMAL introduces no-extra inference cost(Tab.3). 

Tab.2 Comparison with frequency method in LOL v2-syn.
||FECNet|FECNet+MMAL|FourLLIE'23|FourLLIE+MMAL|WaveMamba'24|WaveMamba+MMAL|RetinexFormer+MMAL
-|-|-|-|-|-|-|-
PSNR/SSIM|22.764/.899|23.35/.912|23.14/.88|23.54/.91|23.32/.885|24.16/.914|26.63/.944
## RQ3@Comparisons with losses funcs.
In Tab.3, MMAL outperforms both FFL & LPIPS(VGG), with better PSNR/SSIM and structure preservation. 

Tab.3 Diff loss(RetinexFormer,LOLv2-syn).
||Baseline|FFL|LPIPS(VGG)|MMAL
-|-|-|-|-
PSNR/SSIM|25.67/.93|23.58/.858|26.29.932|26.63/.944
Train/Infer(ms)|48.7/7.2|49.7/7.2|55.2/7.2|54.3/7.2
FLOPS(G)|15.57|15.60|55.68|15.96
Params(M)|1.61|1.61|14.72|1.61
## RQ4@comparisons with frequency-domain func.
MMAL significantly improves baseline performance (Tab.2) and structural benefits beyond frequency priors, approaching RetinexFormer+MMAL.
## Minor Issues@Writing issues.
Thanks for pointing out. We have checked and revised the $\sigma^2$ definition, notation consistency, and typos as suggested.

