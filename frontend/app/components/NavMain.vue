<script setup lang="ts">
import type { Component } from "vue"
import { IconLayoutDashboard, IconMail } from "@tabler/icons-vue"

import { Button } from "@/components/ui/button"
import {
    SidebarGroup,
    SidebarGroupContent,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
} from "@/components/ui/sidebar"

interface NavItem {
    title: string
    url: string
    icon?: Component
    iconAfter?: Component
}

defineProps<{
    items: NavItem[]
}>()
</script>

<template>
    <SidebarGroup>
        <SidebarGroupContent class="flex flex-col gap-2">
            <SidebarMenu>
                <SidebarMenuItem class="flex items-center gap-2">
                    <SidebarMenuButton tooltip="Dashboard"
                        class="bg-primary text-primary-foreground hover:bg-primary/90 hover:text-primary-foreground active:bg-primary/90 active:text-primary-foreground min-w-8 duration-200 ease-linear">
                        <IconLayoutDashboard />
                        <span>Dashboard</span>
                    </SidebarMenuButton>

                </SidebarMenuItem>

            </SidebarMenu>
            <SidebarMenu>
                <SidebarMenuItem class="flex items-center gap-2" v-for="item in items" :key="item.title">
                    <SidebarMenuButton :tooltip="item.title">
                        <component :is="item.icon" v-if="item.icon" />
                        <span>{{ item.title }}</span>
                    </SidebarMenuButton>
                    <Button v-if="item.iconAfter" size="icon" class="size-8 group-data-[collapsible=icon]:opacity-0"
                        variant="outline">
                        <component :is="item.iconAfter" />
                        <span class="sr-only">Inbox</span>
                    </Button>

                </SidebarMenuItem>

            </SidebarMenu>
        </SidebarGroupContent>
    </SidebarGroup>
</template>
