package fr.tathan.common.blocks;


import net.minecraft.core.BlockPos;
import net.minecraft.network.chat.Component;
import net.minecraft.stats.Stats;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.LightningBolt;
import net.minecraft.world.entity.animal.Wolf;
import net.minecraft.world.entity.item.ItemEntity;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.item.enchantment.Enchantment;
import net.minecraft.world.item.enchantment.Enchantments;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.state.BlockState;
import org.jetbrains.annotations.Nullable;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Random;

/** On créer un Block qui extends de Block car c'est un block**/
public class LuckyBlock extends Block {

    /** Le constructeur, permet de mettre des valeurs customs **/
    public LuckyBlock(Properties properties) {
        super(properties);
    }


    /** La method qui s'execute quand un joueur casse un block **/
    @Override
    public void playerDestroy(Level level, Player player, BlockPos blockPos, BlockState blockState, @Nullable BlockEntity blockEntity, ItemStack itemStack) {

        if(level.isClientSide()) return;

        Random random = new Random();
        int id = random.nextInt(15);
        if (id == 1 || id == 0) {

            List<ItemStack> entities = List.of(new ItemStack(Items.IRON_SWORD), new ItemStack(Items.IRON_CHESTPLATE), new ItemStack(Items.IRON_LEGGINGS), new ItemStack(Items.IRON_BOOTS), new ItemStack(Items.IRON_HELMET));

            for (ItemStack stack : entities) {
                level.addFreshEntity(new ItemEntity(level, blockPos.getX(), blockPos.getY(), blockPos.getZ(), stack));
            }


        } else if (id == 2) {

            List<ItemStack> stacks = new java.util.ArrayList<>(List.of());
            stacks.add(new ItemStack(Items.NETHERITE_SWORD));
            stacks.add(new ItemStack(Items.IRON_CHESTPLATE));
            stacks.add(new ItemStack(Items.DIAMOND_BOOTS));
            stacks.add(new ItemStack(Items.LEATHER_HELMET));
            stacks.add(new ItemStack(Items.GOLDEN_LEGGINGS));

            for (ItemStack stack : stacks) {
                level.addFreshEntity(new ItemEntity(level, blockPos.getX(), blockPos.getY(), blockPos.getZ(), stack));
            }

        } else if (id == 3) {

            for (int i = 1; i < 4; i++) {
                Wolf wolf = new Wolf(EntityType.WOLF, level);
                wolf.setPos(blockPos.getX(), blockPos.getY(), blockPos.getZ());
                level.addFreshEntity(wolf);
            }

            ItemStack bones = new ItemStack(Items.BONE);
            bones.setHoverName(Component.nullToEmpty("Boner"));
            bones.setCount(32);
            player.getInventory().add(bones);

        } else if (id == 4) {

            ItemStack knockback = new ItemStack(Items.IRON_SWORD);
            knockback.setHoverName(Component.nullToEmpty("Knockback"));
            knockback.enchant(Enchantments.KNOCKBACK, 20);
            player.getInventory().add(knockback);
        } else if (id == 5) {

            ItemStack arc = new ItemStack(Items.BOW);
            arc.enchant(Enchantments.MULTISHOT, 3);
            arc.enchant(Enchantments.FLAMING_ARROWS, 3);

            player.getInventory().add(arc);

            ItemStack arrow = new ItemStack(Items.SPECTRAL_ARROW);
            arrow.setCount(64);
            player.getInventory().add(arrow);

        } else if (id == 6) {

            List<ItemStack> entities = List.of(new ItemStack(Items.GOLDEN_LEGGINGS), new ItemStack(Items.GOLDEN_CHESTPLATE), new ItemStack(Items.GOLDEN_BOOTS), new ItemStack(Items.GOLDEN_HELMET), new ItemStack(Items.GOLDEN_AXE));

            for (ItemStack stack : entities) {
                level.addFreshEntity(new ItemEntity(level, blockPos.getX(), blockPos.getY(), blockPos.getZ(), stack));
            }

            ItemStack gap = new ItemStack(Items.GOLDEN_APPLE);
            gap.setCount(12);
            player.getInventory().add(gap);

        } else if (id == 7 || id == 8) {
            LightningBolt blot = new LightningBolt( EntityType.LIGHTNING_BOLT, level);
            blot.setPos(blockPos.getX(), blockPos.getY(), blockPos.getZ());
            level.addFreshEntity(blot);
        } else if (id == 9) {

            ItemStack obsidian = new ItemStack(Items.OBSIDIAN);
            obsidian.setCount(5);

            ItemStack water = new ItemStack(Items.WATER_BUCKET);

            ItemStack pearl = new ItemStack(Items.ENDER_PEARL);
            pearl.setCount(6);

            player.getInventory().add(pearl);
            player.getInventory().add(water);
            player.getInventory().add(obsidian);

        } else if (id == 11 || id==12) {
            ItemStack end_portal = new ItemStack(Items.END_PORTAL_FRAME);
            end_portal.setCount(10);

            ItemStack pearl = new ItemStack(Items.ENDER_PEARL);
            pearl.setCount(9);
            ItemStack eye = new ItemStack(Items.ENDER_EYE);
            eye.setCount(8);

            player.getInventory().add(pearl);
            player.getInventory().add(eye);
            player.getInventory().add(end_portal);

        } else if (id == 13) {
            player.setSecondsOnFire(10);
            ItemStack bucket = new ItemStack(Items.WATER_BUCKET);
            player.getInventory().add(bucket);

            player.sendMessage(Component.nullToEmpty("C'est chaud, c'est chaud ! c'est chaud tu es en feu !"), player.getUUID());


        } else {

            Objects.requireNonNull(level.getServer()).getPlayerList().getPlayers().forEach((p) -> {
                p.sendMessage(Component.nullToEmpty(player.getName() + "n'a pas eu de chance ;(. La vie c'est pas kiwi"), p.getUUID());

            });
        }

        /** On appelle la methode de base pour laisser le block se casser **/
        super.playerDestroy(level, player, blockPos, blockState, blockEntity, itemStack);

    }

}